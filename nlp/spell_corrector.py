import re
from collections import Counter, defaultdict

class SpellCorrector:
    """Spelling error detection and correction using edit distance"""
    
    def __init__(self):
        # English dictionary with frequencies (simplified)
        self.english_dict = self._build_english_dictionary()
        
        # Telugu word list (simplified)
        self.telugu_dict = self._build_telugu_dictionary()
        
        # Protected words (kingdom names, etc.)
        self.protected_words = set()
    
    def _build_english_dictionary(self):
        """Build English dictionary with word frequencies"""
        # Common English words with relative frequencies
        common_words = {
            'the': 1000, 'of': 800, 'and': 700, 'to': 650, 'a': 600, 'in': 550,
            'is': 500, 'it': 450, 'you': 400, 'that': 350, 'he': 300, 'was': 290,
            'for': 280, 'on': 270, 'are': 260, 'as': 250, 'with': 240, 'his': 230,
            'they': 220, 'i': 210, 'at': 200, 'be': 190, 'this': 180, 'have': 170,
            'from': 160, 'or': 150, 'one': 140, 'had': 130, 'but': 120, 'word': 110,
            'not': 100, 'what': 95, 'all': 90, 'were': 85, 'we': 80, 'when': 75,

            
            'your': 70, 'can': 65, 'said': 60, 'there': 55, 'each': 50, 'which': 45,
            'do': 40, 'how': 35, 'their': 30, 'if': 25, 'will': 20, 'way': 15,
            'about': 14, 'out': 13, 'many': 12, 'then': 11, 'them': 10,
            # History-related words
            'kingdom': 50, 'king': 45, 'dynasty': 40, 'empire': 35, 'ruler': 30,
            'history': 40, 'ancient': 35, 'medieval': 25, 'capital': 30, 'war': 25,
            'battle': 20, 'conquest': 15, 'territory': 20, 'culture': 25, 'temple': 20,
            'architecture': 15, 'religion': 20, 'trade': 18, 'administration': 12 , 'queen':10
        }
        
        return common_words
    
    def _build_telugu_dictionary(self):
        """Build Telugu dictionary with word frequencies"""
        # Common Telugu words with relative frequencies
        telugu_words = {
            # Common words
            'అది': 100, 'ఇది': 95, 'ఆయన': 90, 'ఈయన': 85, 'అలా': 80, 'ఇలా': 75,
            'ఎప్పుడు': 70, 'ఎక్కడ': 65, 'ఎలా': 60, 'ఎందుకు': 55, 'ఏమిటి': 50,
            'చాలా': 90, 'కొంచం': 40, 'మరింత': 35, 'అన్ని': 45, 'కొన్ని': 40,
            'మొదటి': 35, 'చివరి': 30, 'కొత్త': 40, 'పాత': 35,
            # History-related Telugu words
            'రాజ్యం': 50, 'రాజు': 45, 'వంశం': 40, 'సామ్రాజ్యం': 35, 'పాలకుడు': 30,
            'చరిత్ర': 40, 'పురాతన': 35, 'మధ్యయుగ': 25, 'రాజధాని': 30, 'యుద్ధం': 25,
            'పోరాటం': 20, 'జయం': 18, 'భూభాగం': 20, 'సంస్కృతి': 25, 'ఆలయం': 20,
            'వాస్తుకళ': 15, 'మతం': 20, 'వాణిజ్యం': 18, 'పాలన': 22,
            # Specific kingdoms
            'కాకతీయులు': 30, 'కాకతీయ': 25, 'శాతవాహనులు': 25, 'శాతవాహన': 20,
            'చాలుక్యులు': 25, 'చాలుక్య': 20, 'రాష్ట్రకూటులు': 20, 'రాష్ట్రకూట': 15,
            'విజయనగర': 25, 'చోళులు': 20, 'చోళ': 15,
            # Rulers and places
            'రుద్రమదేవి': 15, 'గణపతిదేవుడు': 12, 'ప్రతాపరుద్రుడు': 10,
            'వరంగల్': 20, 'హైదరాబాద్': 18, 'విజయవాడ': 15, 'అమరావతి': 12
        }
        
        return telugu_words
    
    def add_protected_words(self, words):
        """Add words that should not be corrected (e.g., kingdom names)"""
        self.protected_words.update(words)
    
    def is_valid_word(self, word, language):
        """Check if word exists in dictionary"""
        if language == 'te':
            return word in self.telugu_dict
        else:
            return word.lower() in self.english_dict
    
    def generate_candidates(self, word):
        """Generate spelling correction candidates using edit distance"""
        letters = 'abcdefghijklmnopqrstuvwxyz'
        
        # Telugu letters for Telugu words
        if any('\u0C00' <= c <= '\u0C7F' for c in word):
            telugu_letters = [
                'అ', 'ఆ', 'ఇ', 'ఈ', 'ఉ', 'ఊ', 'ఋ', 'ఌ', 'ఎ', 'ఏ', 'ఐ', 'ఒ', 'ఓ', 'ఔ',
                'క', 'ఖ', 'గ', 'ఘ', 'ఙ', 'చ', 'ఛ', 'జ', 'ఝ', 'ఞ', 'ట', 'ఠ', 'డ', 'ఢ', 'ణ',
                'త', 'థ', 'ద', 'ధ', 'న', 'ప', 'ఫ', 'బ', 'భ', 'మ', 'య', 'ర', 'ల', 'వ',
                'శ', 'ష', 'స', 'హ', 'ళ'
            ]
            letters = telugu_letters
        
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        
        # Delete one character
        deletes = [L + R[1:] for L, R in splits if R]
        
        # Transpose adjacent characters
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        
        # Replace one character
        replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
        
        # Insert one character
        inserts = [L + c + R for L, R in splits for c in letters]
        
        return set(deletes + transposes + replaces + inserts)
    
    def get_word_probability(self, word, language):
        """Get word probability from dictionary"""
        if language == 'te':
            return self.telugu_dict.get(word, 0)
        else:
            return self.english_dict.get(word.lower(), 0)
    
    def correct_word(self, word, language):
        """Correct a single word using edit distance and probability"""
        # Don't correct if protected
        if word.lower() in self.protected_words:
            return word
        
        # Don't correct if already valid
        if self.is_valid_word(word, language):
            return word
        
        # Don't correct very short words or numbers
        if len(word) < 3 or word.isdigit():
            return word
        
        # Generate candidates
        candidates = self.generate_candidates(word)
        
        # Filter valid candidates
        if language == 'te':
            valid_candidates = [c for c in candidates if c in self.telugu_dict]
        else:
            valid_candidates = [c for c in candidates if c.lower() in self.english_dict]
        
        if not valid_candidates:
            return word  # No valid corrections found
        
        # Score candidates by probability
        def candidate_score(candidate):
            prob = self.get_word_probability(candidate, language)
            # Prefer candidates with smaller edit distance (simpler corrections)
            edit_distance = self._edit_distance(word, candidate)
            penalty = 0.1 ** edit_distance  # Exponential penalty for distance
            return prob * penalty
        
        best_candidate = max(valid_candidates, key=candidate_score)
        return best_candidate
    
    def _edit_distance(self, s1, s2):
        """Calculate edit distance between two strings"""
        if len(s1) < len(s2):
            return self._edit_distance(s2, s1)
        
        if len(s2) == 0:
            return len(s1)
        
        previous_row = list(range(len(s2) + 1))
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        
        return previous_row[-1]
    
    def correct_tokens(self, tokens, language):
        """Correct a list of tokens"""
        corrected = []
        for token in tokens:
            corrected_token = self.correct_word(token, language)
            corrected.append(corrected_token)
        
        return corrected
