import re
import unicodedata

# ---- Fallbacks (used if NLTK stopwords aren't available) ----
EN_FALLBACK_STOPWORDS = set([
    'i','me','my','myself','we','our','ours','ourselves','you','your','yours','yourself','yourselves',
    'he','him','his','himself','she','her','hers','herself','it','its','itself','they','them','their',
    'theirs','themselves','what','which','who','whom','this','that','these','those','am','is','are',
    'was','were','be','been','being','have','has','had','having','do','does','did','doing','a','an',
    'the','and','but','if','or','because','as','until','while','of','at','by','for','with','through',
    'during','before','after','above','below','up','down','in','out','on','off','over','under','again',
    'further','then','once'
])

TE_STOPWORDS = set([
    'అని','అనుకుంటున్నాను','అందులో','అయితే','అయినా','అక్కడ','అటువంటి','అన్ని','అలా','అలానే','అవి','అవే',
    'అంటే','అంతే','అంత','అప్పుడు','ఇది','ఇందులో','ఇలా','ఇలానే','ఇవి','ఇవే','ఇక్కడ','ఇంకా','ఇంట','ఉన్నారు',
    'ఉంది','ఉండి','ఉంటుంది','ఉన్నది','ఉన్న','ఎందుకంటే','ఎప్పుడు','ఎలా','ఎక్కడ','ఏమిటి','ఏది','ఏదో','ఒక',
    'ఒకటి','ఒకసారి','కానీ','కాబట్టి','కూడా','కొన్ని','గురించి','చాలా','చేసి','చేస్తున్నాను','తర్వాత','తెలుసు',
    'దానిని','దేనిని','ద్వారా','నేను','నాకు','నా','నిజంగా','పైన','మళ్లీ','మాత్రమే','మీరు','మీ','యొక్క','రకంగా',
    'వారు','వాటిని','వేరు','సరే','హాయ్'
])

TE_SUFFIXES = (
    'ులు','లు','కు','తో','లో','పై','కి','ని','గా','నా','దు','టు','చు','వు','ము','రు','ను','దా','తా','కా','గు','తు'
)

TELUGU_BLOCK_RE = r'[\u0C00-\u0C7F]+' 

class SimpleEnglishStemmer:
    """Very small stemmer covering the most common English suffix patterns."""

    COMMON_SUFFIXES = (
        'ization','ational','fulness','ousness','iveness','tional','biliti','lessli','entli','ation',
        'alism','aliti','ousli','iviti','fulli','icate','ative','alize','iciti','ical','ness','ment',
        'ence','ance','ship','able','ible','less','ous','ers','ing','est','ies','ied','ily','ily','ed',
        'er','ly','es','s'
    )

    def stem(self, word: str) -> str:
        if len(word) <= 3:
            return word
        lowered = word.lower()

        # Handle a couple of irregular plural/tense patterns first
        if lowered.endswith('ies') and len(word) > 4:
            return lowered[:-3] + 'y'
        if lowered.endswith('ied') and len(word) > 4:
            return lowered[:-3] + 'y'
        if lowered.endswith('ing') and len(word) > 5:
            base = lowered[:-3]
            if base.endswith(base[-1] * 2):
                base = base[:-1]
            return base

        for suffix in self.COMMON_SUFFIXES:
            if lowered.endswith(suffix) and len(word) - len(suffix) >= 3:
                return lowered[:-len(suffix)]
        return lowered


class TextProcessor:
    """Text normalization, tokenization, stopword removal, and stemming for English (en) and Telugu (te)."""

    def __init__(self):
        # English stemmer
        self.stemmer = SimpleEnglishStemmer()

        # English stopwords (use NLTK if available, else fallback)
        self.english_stopwords = EN_FALLBACK_STOPWORDS

        # Telugu stopwords
        self.telugu_stopwords = TE_STOPWORDS

    # ---------- Normalize ----------
    def normalize_text(self, text: str, language: str) -> str:
        """Unicode-NFC, optional lowercasing for English, strip punctuation and collapse spaces."""
        if not text:
            return ""
        text = unicodedata.normalize('NFC', text)
        if language == 'en':
            text = text.lower()
        # Replace punctuation with space, then collapse whitespace
            text = re.sub(r'[^\w\s]', ' ', text)
        return re.sub(r'\s+', ' ', text).strip()

    # ---------- Tokenize ----------
    def tokenize(self, text: str, language: str):
        """Regex-based tokenization: Telugu by script block, English by word boundaries."""
        if not text:
            return []
        if language == 'te':
            tokens = re.findall(TELUGU_BLOCK_RE, text)
        else:
            tokens = re.findall(r'\b\w+\b', text)  # already lowercased in normalize for English
        return [t for t in tokens if t]

    # ---------- Stopword removal ----------
    def remove_stopwords(self, tokens, language: str):
        stop = self.telugu_stopwords if language == 'te' else self.english_stopwords
        return [t for t in tokens if t not in stop]

    # ---------- Stemming ----------
    def stem_tokens(self, tokens, language: str):
        if language == 'en':
            return [self.stemmer.stem(t) for t in tokens]
        # Telugu: simple suffix strip
        return [self._simple_telugu_stem(t) for t in tokens]

    def _simple_telugu_stem(self, word: str) -> str:
        """Very light Telugu stemming by removing common suffixes (guard against over-stemming)."""
        if len(word) <= 3:
            return word
        for suf in TE_SUFFIXES:
            if word.endswith(suf):
                stem = word[:-len(suf)]
                if len(stem) >= 2:
                    return stem
        return word

    # ---------- Full pipeline ----------
    def process_text(self, text: str, language: str, remove_stopwords: bool = True, apply_stemming: bool = False):
        """Normalize → tokenize → (optional) stopword removal → (optional) stemming."""
        normalized = self.normalize_text(text, language)
        tokens = self.tokenize(normalized, language)
        if remove_stopwords:
            tokens = self.remove_stopwords(tokens, language)
        if apply_stemming:
            tokens = self.stem_tokens(tokens, language)
        return {
            "normalized_text": normalized,
            "tokens": tokens,
            "processed_text": " ".join(tokens),
        }
