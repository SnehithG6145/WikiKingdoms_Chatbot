"""
Helper functions and utilities for the kingdom history chatbot
"""

import os
import pickle
from nlp.language_detector import LanguageDetector
from nlp.text_processor import TextProcessor
from nlp.spell_corrector import SpellCorrector
from nlp.intent_detector import IntentDetector
from nlp.retrieval_system import RetrievalSystem
from nlp.query_expander import QueryExpander
from nlp.bigram import NgramSpellChecker
from sample_corpus import get_sample_corpus
from data.gazetteer import get_gazetteer, get_all_protected_words

def initialize_system():
    """Initialize all system components"""
    print("Initializing Kingdom History Chatbot...")
    
    # Initialize components
    print("Loading language detector...")
    lang_detector = LanguageDetector()
    
    print("Loading text processor...")
    text_processor = TextProcessor()
    
    print("Loading spell corrector...")
    spell_corrector = NgramSpellChecker()
    
    # Add protected words from gazetteer
    #protected_words = get_all_protected_words()
    #spell_corrector.add_protected_words(protected_words)
    
    print("Loading gazetteer...")
    gazetteer = get_gazetteer()
    
    print("Loading intent detector...")
    intent_detector = IntentDetector(gazetteer)
    
    print("Loading query expander...")
    query_expander = QueryExpander(gazetteer)
    
    print("Loading corpus data...")
    corpus_data = get_sample_corpus()
    
    print("Building retrieval index...")
    retrieval_system = RetrievalSystem(corpus_data)
    
    
    
    
    
    print("System initialization complete!")
    
    # Print system stats
    stats = retrieval_system.get_index_stats()
    print(f"Index statistics:")
    for lang, lang_stats in stats.items():
        if lang_stats['num_paragraphs'] > 0:
            print(f"  {lang.upper()}: {lang_stats['num_paragraphs']} paragraphs, "
                  f"{lang_stats['num_features']} features")
            print(f"    Kingdoms: {', '.join(lang_stats['kingdoms'])}")
    
    return {
        'language_detector': lang_detector,
        'text_processor': text_processor,
        'spell_corrector': spell_corrector,
        'intent_detector': intent_detector,
        'retrieval_system': retrieval_system,
        'query_expander': query_expander,
        
        
        'gazetteer': gazetteer,
        'corpus_stats': stats
    }

def save_system_state(components, filepath):
    """Save system state to disk"""
    try:
        with open(filepath, 'wb') as f:
            pickle.dump(components, f)
        return True
    except Exception as e:
        print(f"Error saving system state: {e}")
        return False

def load_system_state(filepath):
    """Load system state from disk"""
    try:
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                components = pickle.load(f)
            return components
        return None
    except Exception as e:
        print(f"Error loading system state: {e}")
        return None

def validate_query(query):
    """Validate user query"""
    if not query or not query.strip():
        return False, "Query cannot be empty"
    
    if len(query.strip()) < 2:
        return False, "Query too short"
    
    if len(query) > 1000:
        return False, "Query too long (maximum 1000 characters)"
    
    return True, "Valid"

def format_results_for_display(results, max_results=3):
    """Format retrieval results for display"""
    if not results or 'paragraphs' not in results:
        return []
    
    formatted = []
    for i, result in enumerate(results['paragraphs'][:max_results]):
        formatted_result = {
            'rank': i + 1,
            'text': result['text'],
            'kingdom': result['kingdom'],
            'language': result['language'],
            'similarity': f"{result['similarity']:.3f}",
            'preview': result['text'][:200] + "..." if len(result['text']) > 200 else result['text']
        }
        formatted.append(formatted_result)
    
    return formatted

def get_query_suggestions(language='en'):
    """Get sample query suggestions based on language"""
    if language == 'te':
        suggestions = [
            "కాకతీయ వంశం గురించి చెప్పండి",
            "రుద్రమదేవి ఎవరు?",
            "విజయనగర సామ్రాజ్యం గురించి తెలియజేయండి",
            "కృష్ణదేవరాయల పాలన గురించి చెప్పండి",
            "శాతవాహన రాజ్యం ఎక్కడ ఉండేది?",
            "చోళ వంశంలో ప్రసిద్ధ రాజులు ఎవరు?",
            "వరంగల్ చరిత్ర గురించి తెలుసుకోవాలి",
            "హంపి గురించి చెప్పండి"
        ]
    else:
        suggestions = [
            "Tell me about the Kakatiya dynasty",
            "Who was Rudrama Devi?",
            "What do you know about Vijayanagara Empire?",
            "Tell me about Krishnadevaraya's rule",
            "Where was the Satavahana kingdom located?",
            "Who were the famous rulers of Chola dynasty?",
            "I want to know about Warangal history",
            "Tell me about Hampi"
        ]
    
    return suggestions

def get_kingdom_summary(kingdom_name):
    """Get a brief summary of a kingdom"""
    gazetteer = get_gazetteer()
    
    if kingdom_name in gazetteer:
        kingdom_data = gazetteer[kingdom_name]
        
        summary = {
            'name': kingdom_name,
            'primary_names': kingdom_data.get('primary_names', [])[:2],  # First 2 names
            'key_rulers': kingdom_data.get('rulers', [])[:3],  # First 3 rulers
            'important_places': kingdom_data.get('places', [])[:3],  # First 3 places
            'available_languages': ['en', 'te'] if any('en' in name for name in kingdom_data.get('primary_names', [])) else ['en']
        }
        
        return summary
    
    return None

def detect_language_simple(text):
    """Simple language detection for display purposes"""
    # Count Telugu characters
    telugu_chars = sum(1 for c in text if '\u0C00' <= c <= '\u0C7F')
    total_chars = len([c for c in text if c.isalpha()])
    
    if total_chars == 0:
        return 'en'
    
    telugu_ratio = telugu_chars / total_chars
    return 'te' if telugu_ratio > 0.3 else 'en'

def clean_text_for_display(text, max_length=500):
    """Clean and truncate text for display"""
    if not text:
        return ""
    
    # Remove extra whitespace
    cleaned = ' '.join(text.split())
    
    # Truncate if too long
    if len(cleaned) > max_length:
        cleaned = cleaned[:max_length] + "..."
    
    return cleaned

def get_error_message(error_type, language='en'):
    """Get localized error messages"""
    error_messages = {
        'en': {
            'no_results': "No relevant information found for your query.",
            'query_too_short': "Please enter a longer query (at least 3 characters).",
            'query_too_long': "Query is too long. Please keep it under 1000 characters.",
            'system_error': "An error occurred while processing your query.",
            'no_kingdom_detected': "Could not identify which kingdom you're asking about.",
            'language_detection_failed': "Could not detect the language of your query."
        },
        'te': {
            'no_results': "మీ ప్రశ్నకు సంబంధించిన సమాచారం దొరకలేదు.",
            'query_too_short': "దయచేసి పొడవైన ప్రశ్న వేయండి (కనీసం 3 అక్షరాలు).",
            'query_too_long': "ప్రశ్న చాలా పొడవుగా ఉంది. దయచేసి 1000 అక్షరాలలోపు ఉంచండి.",
            'system_error': "మీ ప్రశ్నను ప్రాసెస్ చేయడంలో లోపం జరిగింది.",
            'no_kingdom_detected': "మీరు ఏ రాజ్యం గురించి అడుగుతున్నారో గుర్తించలేకపోయాము.",
            'language_detection_failed': "మీ ప్రశ్న యొక్క భాషను గుర్తించలేకపోయాము."
        }
    }
    
    return error_messages.get(language, error_messages['en']).get(error_type, error_messages['en']['system_error'])

# Performance monitoring functions
def log_query_performance(query, language, processing_time, results_count):
    """Log query performance metrics"""
    # In a production system, this would log to a proper logging system
    print(f"Query processed: lang={language}, time={processing_time:.3f}s, results={results_count}")

def get_system_health():
    """Get system health status"""
    return {
        'status': 'healthy',
        'components_loaded': True,
        'index_ready': True,
        'timestamp': None  # Would be actual timestamp in production
    }
