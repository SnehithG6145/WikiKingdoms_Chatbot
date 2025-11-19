import re
import unicodedata
from collections import Counter

class LanguageDetector:
    """Detect language (Telugu/English) using Unicode script detection"""
    
    def __init__(self):
        # Telugu Unicode range
        self.telugu_range = (0x0C00, 0x0C7F)
        
        # Character n-gram profiles for fallback
        self.char_profiles = {
            'te': self._build_telugu_profile(),
            'en': self._build_english_profile()
        }
    
    def _build_telugu_profile(self):
        """Build character n-gram profile for Telugu"""
        # Common Telugu character patterns
        common_chars = [
            'అ', 'ఆ', 'ఇ', 'ఈ', 'ఉ', 'ఊ', 'ఋ', 'ఌ', 'ఎ', 'ఏ', 'ఐ', 'ఒ', 'ఓ', 'ఔ',
            'క', 'ఖ', 'గ', 'ఘ', 'ఙ', 'చ', 'ఛ', 'జ', 'ఝ', 'ఞ', 'ట', 'ఠ', 'డ', 'ఢ', 'ణ',
            'త', 'థ', 'ద', 'ధ', 'న', 'ప', 'ఫ', 'బ', 'భ', 'మ', 'య', 'ర', 'ల', 'వ',
            'శ', 'ష', 'స', 'హ', 'ళ', 'క్ష', 'జ్ఞ'
        ]
        
        # Common Telugu bigrams
        common_bigrams = [
            'అన', 'అర', 'ఇన', 'ఉన', 'ఎల', 'కా', 'కి', 'కు', 'గా', 'చా', 'చి', 'చు',
            'తా', 'తి', 'తు', 'దా', 'దు', 'నా', 'ని', 'ను', 'పా', 'పి', 'పు', 'మా',
            'మి', 'ము', 'యా', 'యు', 'రా', 'రి', 'రు', 'లా', 'లి', 'లు', 'వా', 'వి',
            'వు', 'సా', 'సి', 'సు', 'హా', 'హి', 'హు'
        ]
        
        profile = {}
        for char in common_chars:
            profile[char] = 0.02  # Base frequency
        for bigram in common_bigrams:
            profile[bigram] = 0.01
            
        return profile
    
    def _build_english_profile(self):
        """Build character n-gram profile for English"""
        # Common English character frequencies
        common_chars = 'etaoinshrdlcumwfgypbvkjxqz'
        common_bigrams = [
            'th', 'he', 'in', 'er', 'an', 're', 'ed', 'nd', 'on', 'en', 'at', 'ou',
            'ea', 'ha', 'ng', 'as', 'or', 'ti', 'is', 'et', 'it', 'ar', 'te', 'st',
            'es', 'le', 'of', 'to', 'nt', 'hi', 'se', 've'
        ]
        
        profile = {}
        for i, char in enumerate(common_chars):
            profile[char] = (26 - i) / 350.0  # Decreasing frequency
        for bigram in common_bigrams:
            profile[bigram] = 0.015
            
        return profile
    
    def detect_language(self, text):
        """
        Detect language of input text
        Returns: dict with 'language' and 'confidence'
        """
        if not text.strip():
            return {'language': 'en', 'confidence': 0.5}
        
        # Primary method: Unicode script detection
        unicode_result = self._unicode_script_detection(text)
        
        if unicode_result['confidence'] > 0.7:
            return unicode_result
        
        # Fallback: Character n-gram scoring
        ngram_result = self._ngram_scoring(text)
        
        # Combine results
        if unicode_result['confidence'] > 0.5:
            return unicode_result
        else:
            return ngram_result
    
    def _unicode_script_detection(self, text):
        """Detect language based on Unicode script ranges"""
        telugu_count = 0
        latin_count = 0
        total_letters = 0
        
        for char in text:
            code_point = ord(char)
            
            # Check if it's Telugu
            if self.telugu_range[0] <= code_point <= self.telugu_range[1]:
                telugu_count += 1
                total_letters += 1
            # Check if it's Latin (English)
            elif char.isalpha() and char.isascii():
                latin_count += 1
                total_letters += 1
        
        if total_letters == 0:
            return {'language': 'en', 'confidence': 0.5}
        
        telugu_ratio = telugu_count / total_letters
        latin_ratio = latin_count / total_letters
        
        if telugu_ratio > latin_ratio:
            return {'language': 'te', 'confidence': telugu_ratio}
        else:
            return {'language': 'en', 'confidence': latin_ratio}
    
    def _ngram_scoring(self, text):
        """Fallback method using character n-gram scoring"""
        text = text.lower()
        
        te_score = 0.0
        en_score = 0.0
        
        # Unigram scoring
        for char in text:
            if char in self.char_profiles['te']:
                te_score += self.char_profiles['te'][char]
            if char in self.char_profiles['en']:
                en_score += self.char_profiles['en'][char]
        
        # Bigram scoring
        for i in range(len(text) - 1):
            bigram = text[i:i+2]
            if bigram in self.char_profiles['te']:
                te_score += self.char_profiles['te'][bigram]
            if bigram in self.char_profiles['en']:
                en_score += self.char_profiles['en'][bigram]
        
        total_score = te_score + en_score
        if total_score == 0:
            return {'language': 'en', 'confidence': 0.5}
        
        if te_score > en_score:
            confidence = te_score / total_score
            return {'language': 'te', 'confidence': confidence}
        else:
            confidence = en_score / total_score
            return {'language': 'en', 'confidence': confidence}
