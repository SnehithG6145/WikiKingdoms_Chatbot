import math
import os
import pickle
import hashlib
from collections import Counter, OrderedDict, defaultdict

class RetrievalSystem:
    """
    TF-IDF based retrieval system (manual implementation) with cosine similarity
    Works for both English (word-level) and Telugu (char-level n-grams)
    """

    def __init__(self, corpus_data=None, cache_size=100):
        self.corpus_data = corpus_data or []
        self.vectorizers = {'en': None, 'te': None}
        self.tfidf_matrices = {'en': None, 'te': None}
        self.paragraph_metadata = {'en': [], 'te': []}

        # Cache system
        self.cache_size = cache_size
        self.query_cache = OrderedDict()
        self.cache_hits = 0
        self.cache_misses = 0

        if corpus_data:
            self.build_index()

    # ---------------------------------------------------------
    #  Basic text processing
    # ---------------------------------------------------------
    def _tokenize_en(self, text):
        # Simple English tokenizer: split on spaces and punctuation
        tokens = []
        word = ""
        for ch in text.lower():
            if ch.isalpha():
                word += ch
            else:
                if word:
                    tokens.append(word)
                    word = ""
        if word:
            tokens.append(word)
        return tokens

    def _char_ngrams_te(self, text, n_range=(2,4)):
        # Telugu: use character n-grams
        text = text.strip()
        ngrams = []
        for n in range(n_range[0], n_range[1]+1):
            for i in range(len(text) - n + 1):
                ngrams.append(text[i:i+n])
        return ngrams or [text]  # fallback if too short

    # ---------------------------------------------------------
    #  Build the TF-IDF index manually
    # ---------------------------------------------------------
    def build_index(self):
        en_docs = [d for d in self.corpus_data if d['language'] == 'en']
        te_docs = [d for d in self.corpus_data if d['language'] == 'te']

        if en_docs:
            self._build_language_index(en_docs, 'en')
        if te_docs:
            self._build_language_index(te_docs, 'te')

    def _build_language_index(self, data, language):
        """
        Build TF-IDF manually for a specific language
        """
        texts = [item['text'] for item in data]

        # Tokenize each paragraph
        tokenized_docs = []
        for text in texts:
            if language == 'te':
                tokens = self._char_ngrams_te(text)
            else:
                tokens = self._tokenize_en(text)
            tokenized_docs.append(tokens)

        # Compute document frequencies
        df = Counter()
        for tokens in tokenized_docs:
            unique_terms = set(tokens)
            for term in unique_terms:
                df[term] += 1

        num_docs = len(tokenized_docs)
        # Compute IDF
        idf = {term: math.log((1 + num_docs) / (1 + freq)) + 1 for term, freq in df.items()}

        # Build TF-IDF matrix
        tfidf_vectors = []
        for tokens in tokenized_docs:
            tf = Counter(tokens)
            total_terms = sum(tf.values()) or 1
            tfidf = {}
            for term, freq in tf.items():
                tfidf[term] = (freq / total_terms) * idf.get(term, 0)
            tfidf_vectors.append(tfidf)

        # Save to class
        self.tfidf_matrices[language] = tfidf_vectors
        self.vectorizers[language] = {'idf': idf, 'terms': list(idf.keys())}
        self.paragraph_metadata[language] = data

    # ---------------------------------------------------------
    #  Cache utilities
    # ---------------------------------------------------------
    def _generate_cache_key(self, query, language, target_kingdoms, top_k):
        kingdoms_str = ','.join(sorted(target_kingdoms)) if target_kingdoms else 'all'
        key_str = f"{query}|{language}|{kingdoms_str}|{top_k}"
        return hashlib.md5(key_str.encode()).hexdigest()

    def _get_from_cache(self, key):
        if key in self.query_cache:
            self.cache_hits += 1
            self.query_cache.move_to_end(key)
            return self.query_cache[key]
        self.cache_misses += 1
        return None

    def _add_to_cache(self, key, result):
        self.query_cache[key] = result
        self.query_cache.move_to_end(key)
        if len(self.query_cache) > self.cache_size:
            self.query_cache.popitem(last=False)

    def get_cache_stats(self):
        total = self.cache_hits + self.cache_misses
        hit_rate = (self.cache_hits / total * 100) if total else 0
        return {
            'cache_size': len(self.query_cache),
            'max_cache_size': self.cache_size,
            'hits': self.cache_hits,
            'misses': self.cache_misses,
            'hit_rate': hit_rate
        }

    # ---------------------------------------------------------
    #  Manual cosine similarity
    # ---------------------------------------------------------
    def _cosine_similarity(self, vec1, vec2):
        all_terms = set(vec1.keys()) | set(vec2.keys())
        dot = sum(vec1.get(t, 0) * vec2.get(t, 0) for t in all_terms)
        norm1 = math.sqrt(sum(v**2 for v in vec1.values()))
        norm2 = math.sqrt(sum(v**2 for v in vec2.values()))
        if norm1 == 0 or norm2 == 0:
            return 0.0
        return dot / (norm1 * norm2)

    # ---------------------------------------------------------
    #  Query Vectorization
    # ---------------------------------------------------------
    def _vectorize_query(self, query, language):
        if language == 'te':
            tokens = self._char_ngrams_te(query)
        else:
            tokens = self._tokenize_en(query)

        tf = Counter(tokens)
        total = sum(tf.values()) or 1
        idf = self.vectorizers[language]['idf']
        tfidf_query = {t: (freq / total) * idf.get(t, 0) for t, freq in tf.items()}
        return tfidf_query

    # ---------------------------------------------------------
    #  Search Logic
    # ---------------------------------------------------------
    def search(self, query, language, target_kingdoms=None, top_k=5):
        if not self.tfidf_matrices[language]:
            return {'paragraphs': [], 'query': query, 'language': language}

        cache_key = self._generate_cache_key(query, language, target_kingdoms, top_k)
        cached = self._get_from_cache(cache_key)
        if cached:
            cached['from_cache'] = True
            return cached

        try:
            query_vec = self._vectorize_query(query, language)
            candidates = self.paragraph_metadata[language]

            # Filter by kingdoms if needed
            if target_kingdoms:
                candidates = [c for c in candidates if c['kingdom_label'] in target_kingdoms]
                tfidf_docs = [self.tfidf_matrices[language][i]
                              for i, c in enumerate(self.paragraph_metadata[language])
                              if c['kingdom_label'] in target_kingdoms]
            else:
                tfidf_docs = self.tfidf_matrices[language]

            # Compute similarities
            results = []
            for idx, doc_vec in enumerate(tfidf_docs):
                sim = self._cosine_similarity(query_vec, doc_vec)
                if sim > 0.01:
                    results.append({
                        'text': candidates[idx]['text'],
                        'kingdom': candidates[idx]['kingdom_label'],
                        'language': candidates[idx]['language'],
                        'paragraph_id': candidates[idx].get('paragraph_id', idx),
                        'similarity': round(sim, 4)
                    })

            # Sort by similarity
            results.sort(key=lambda x: x['similarity'], reverse=True)
            result_data = {
                'paragraphs': results[:top_k],
                'query': query,
                'language': language,
                'target_kingdoms': target_kingdoms,
                'total_candidates': len(candidates),
                'from_cache': False
            }

            self._add_to_cache(cache_key, result_data)
            return result_data

        except Exception as e:
            print(f"Search error: {e}")
            return {'paragraphs': [], 'query': query, 'language': language}

    # ---------------------------------------------------------
    #  Save / Load index
    # ---------------------------------------------------------
    def save_index(self, filepath):
        data = {
            'vectorizers': self.vectorizers,
            'tfidf_matrices': self.tfidf_matrices,
            'paragraph_metadata': self.paragraph_metadata
        }
        with open(filepath, 'wb') as f:
            pickle.dump(data, f)

    def load_index(self, filepath):
        if not os.path.exists(filepath):
            return False
        with open(filepath, 'rb') as f:
            data = pickle.load(f)
            self.vectorizers = data['vectorizers']
            self.tfidf_matrices = data['tfidf_matrices']
            self.paragraph_metadata = data['paragraph_metadata']
        return True

    # ---------------------------------------------------------
    #  Stats and utilities
    # ---------------------------------------------------------
    def get_index_stats(self):
        stats = {}
        for lang in ['en', 'te']:
            tfidf = self.tfidf_matrices[lang]
            stats[lang] = {
                'num_paragraphs': len(tfidf) if tfidf else 0,
                'num_features': len(self.vectorizers[lang]['idf']) if self.vectorizers[lang] else 0,
                'kingdoms': list(set(d['kingdom_label'] for d in self.paragraph_metadata[lang]))
            }
        return stats

    def add_documents(self, new_docs):
        self.corpus_data.extend(new_docs)
        self.build_index()

    def search_cross_language(self, query, query_language, top_k=5):
        results_same = self.search(query, query_language, top_k=top_k//2)
        other = 'te' if query_language == 'en' else 'en'
        results_other = self.search(query, other, top_k=top_k//2)

        all_results = results_same['paragraphs'] + results_other['paragraphs']
        all_results.sort(key=lambda x: x['similarity'], reverse=True)

        return {
            'paragraphs': all_results[:top_k],
            'query': query,
            'query_language': query_language,
            'cross_language_search': True
        }
