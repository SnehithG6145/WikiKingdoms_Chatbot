import json
from collections import defaultdict
import math


class NgramSpellChecker:
    def __init__(self):
        """
        Initialize the N-gram spell checker.
        """
        
        self.unigram_map = defaultdict(set)
        self.bigram_map = defaultdict(set)
        self.trigram_map = defaultdict(set)
        self.word_counts = {}
        self.max_word_count = 0  # For frequency normalization

    def load_json(self, language):
        """Load the JSON file with words and their counts."""
        if language == "te":
            json_file = "telugu_word_count.json"
        elif language == "en":
            json_file = "english_word_counts.json"
        else:
            print(f"Warning: No JSON file for language '{language}'. Spell checker will be inactive.")
            self.word_counts = {}
            self.max_word_count = 0
            return # Stop here

        try:
            with open(json_file, "r", encoding="utf-8") as f:
                self.word_counts = json.load(f)
        except FileNotFoundError:
            print(f"Error: Could not find {json_file}. Spell checker will be inactive.")
            self.word_counts = {}
            self.max_word_count = 0
            return

        # 🎯 FIX 1: Calculate max_word_count for normalization
        if self.word_counts:
            self.max_word_count = max(self.word_counts.values())
        else:
            self.max_word_count = 0

        # 🎯 FIX 2: Build the index after loading words
        # Clear old indices first in case this is called multiple times
        self.unigram_map.clear()
        self.bigram_map.clear()
        self.trigram_map.clear()
        
        # This function was never being called before!
        self.build_index()

    def generate_ngrams(self, word, n):
        """Generate n-grams for a given word."""
        return [word[i:i+n] for i in range(len(word) - n + 1)]

    def build_index(self):
        """Build uni-gram, bi-gram, and tri-gram indices."""
        print(f"Building n-gram index for {len(self.word_counts)} words...")
        for word in self.word_counts.keys():
            for n in [1, 2, 3]:
                for ngram in self.generate_ngrams(word, n):
                    if n == 1:
                        self.unigram_map[ngram].add(word)
                    elif n == 2:
                        self.bigram_map[ngram].add(word)
                    else:
                        self.trigram_map[ngram].add(word)

    def get_candidates(self, error_word, n=2):
        """Return set of candidate words that share at least one n-gram with the error word."""
        ngram_map = {1: self.unigram_map, 2: self.bigram_map, 3: self.trigram_map}.get(n)
        if ngram_map is None:
            raise ValueError("n must be 1, 2, or 3")

        candidates = set()
        for ngram in self.generate_ngrams(error_word, n):
            candidates.update(ngram_map.get(ngram, set()))
        return candidates

    def jaccard_similarity(self, word1, word2, n=2):
        """Compute Jaccard similarity between two words based on n-grams."""
        ngrams1 = set(self.generate_ngrams(word1, n))
        ngrams2 = set(self.generate_ngrams(word2, n))
        intersection = ngrams1 & ngrams2
        union = ngrams1 | ngrams2
        return len(intersection) / len(union) if union else 0

    # ✅ Replaced library call with this in-built version
    def _levenshtein(self, a: str, b: str, max_dist: int = 2) -> int:
        """Compute Levenshtein edit distance between two strings (optimized)."""
        if a == b:
            return 0
        if abs(len(a) - len(b)) > max_dist:
            return max_dist + 1
        prev = list(range(len(b) + 1))
        for i, ca in enumerate(a, start=1):
            cur = [i]
            best = cur[0]
            for j, cb in enumerate(b, start=1):
                cost = 0 if ca == cb else 1
                cur.append(min(prev[j] + 1, cur[j-1] + 1, prev[j-1] + cost))
                best = min(best, cur[-1])
            if best > max_dist:
                return max_dist + 1
            prev = cur
        return prev[-1]

    def get_top_candidates(self, error_word, n=2, top_k=3):
        """
        Return top_k candidate words based on a combined score of
        Jaccard, Levenshtein, and word frequency.
        """
        candidates = self.get_candidates(error_word, n)
        scored = []

        # 🎯 FIX 3: Check max_word_count > 0, not == 0
        if not candidates or self.max_word_count == 0:
            return []

        for cand in candidates:
            # 1. Jaccard Score
            jaccard = self.jaccard_similarity(error_word, cand, n)

            # 2. Custom Levenshtein distance
            edit_dist = self._levenshtein(error_word, cand, max_dist=5)
            edit_score = 1.0 / (1.0 + edit_dist)

            # 3. Frequency Score
            freq_score = math.log1p(self.word_counts.get(cand, 0)) / math.log1p(self.max_word_count)

            # 4. Weighted combination
            W_JACCARD = 0.3
            W_EDIT = 0.5
            W_FREQ = 0.2

            final_score = (W_JACCARD * jaccard) + \
                            (W_EDIT * edit_score) + \
                            (W_FREQ * freq_score)

            scored.append((cand, final_score))

        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_k]

    def get_confident_words(self, error_word, top_k=3):
        """Intersection of top uni-, bi-, and tri-gram candidates."""
        top_uni = self.get_top_candidates(error_word, n=1, top_k=top_k)
        top_bi = self.get_top_candidates(error_word, n=2, top_k=top_k)
        top_tri = self.get_top_candidates(error_word, n=3, top_k=top_k)

        # print(f"Top {top_k} Uni-gram candidates: {top_uni}")
        # print(f"Top {top_k} Bi-gram candidates: {top_bi}")
        # print(f"Top {top_k} Tri-gram candidates: {top_tri}")

        uni_dict = dict(top_uni)
        bi_dict = dict(top_bi)
        tri_dict = dict(top_tri)

        common_words = set(uni_dict.keys()) & set(bi_dict.keys()) & set(tri_dict.keys())

        result = []
        if common_words:
            # print(f"Found {len(common_words)} common word(s): {common_words}")
            for word in common_words:
                avg_conf = (uni_dict[word] + bi_dict[word] + tri_dict[word]) / 3
                result.append((word, avg_conf))
            result.sort(key=lambda x: x[1], reverse=True)
        else:
            # print("No common words found — returning top Bi-gram candidate.")
            if top_bi:
                result.append(top_bi[0])

        return result
    
    def get_confident_words_tokens(self, error_tokens, top_k=3):
        """Get confident words for a list of error tokens."""
        all_confident = {}
        for token in error_tokens:
            confident_words = self.get_confident_words(token, top_k=top_k)
            all_confident[token] = confident_words
        return all_confident


# # ================= Example usage =================
# if __name__ == "__main__":
#     # Note: You must have 'telugu_word_count.json' and 'english_word_counts.json'
#     # in the same directory as this script for this test to work.

#     print("=== TELUGU ===")
#     telugu_index = NgramSpellChecker()
#     telugu_index.load_json(language="te") # 🎯 This now builds the index
#     error_word_telugu = "కక్తయ"  # Typo for కాకతీయ
#     print(f"Error word: '{error_word_telugu}'")
#     print("Telugu Confident words:", telugu_index.get_confident_words(error_word_telugu))

#     print("\n---\n")

#     print("=== ENGLISH ===")
#     english_index = NgramSpellChecker()
#     english_index.load_json(language="en") # 🎯 This now builds the index

#     error_word_english_1 = "catured"  # Typo for 'captured'
#     print(f"Error word: '{error_word_english_1}'")
#     print("English Confident words:", english_index.get_confident_words(error_word_english_1))

#     print("\n---\n")

#     error_word_english_2 = "catred"
#     print(f"Error word: '{error_word_english_2}'")
#     print("English Confident words:", english_index.get_confident_words(error_word_english_2))