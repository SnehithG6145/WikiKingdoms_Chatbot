import streamlit as st

from utils.helpers import initialize_system # This loads the components

# Page configuration # streamlit component
st.set_page_config(
    page_title="Kingdom History Chatbot",
    page_icon="🏛️",
    layout="wide"
)

# Initialize system components
@st.cache_resource
def load_system():
    """Initialize and cache all system components"""
    return initialize_system()

def main():
    st.title("🏛️ Kingdom History Chatbot")
    st.markdown("Ask questions about historical kingdoms in Telugu or English!")
    
    # Load system components
    try:
        components = load_system()
        lang_detector = components['language_detector']
        text_processor = components['text_processor']
        spell_corrector = components['spell_corrector'] # This is the NgramSpellChecker instance
        intent_detector = components['intent_detector']
        retrieval_system = components['retrieval_system']
        query_expander = components['query_expander']
        
        
    except Exception as e:
        st.error(f"Failed to initialize system: {str(e)}")
        st.stop()
    
    # Create two columns for layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # User input
        user_query = st.text_area(
            "Enter your question about kingdoms:",
            placeholder="Example: Tell me about Kakatiya dynasty / కాకతీయ వంశం గురించి చెప్పండి",
            height=100
        )
        
        if st.button("Search", type="primary"):
            if user_query.strip():
                process_query(user_query, lang_detector, text_processor, 
                              spell_corrector, intent_detector, retrieval_system, 
                              query_expander)
            else:
                st.warning("Please enter a question!")
    
    with col2:
        st.markdown("### Supported Kingdoms")
        st.markdown("""
        - Kakatiya (కాకతీయులు)
        - Satavahana (శాతవాహనులు)  
        - Chalukya (చాలుక్యులు)
        - Rashtrakuta (రాష్ట్రకూటులు)
        - Vijayanagara (విజయనగర)
        - Chola (చోళులు)
        """)
        
        st.markdown("### Languages")
        st.markdown("- Telugu (తెలుగు)")
        st.markdown("- English")


def process_query(query, lang_detector, text_processor, spell_corrector, 
                  intent_detector, retrieval_system, query_expander):
    """Process user query through the NLP pipeline"""
    
    with st.spinner("Processing your query..."):
        # Step 1: Language Detection
        lang_result = lang_detector.detect_language(query)
        detected_lang = lang_result['language']
        lang_confidence = lang_result['confidence']
        st.markdown(f"**Detected Language:** {detected_lang.upper()} (Confidence: {lang_result['confidence']:.2f})")
        
        
        # Step 2: Text Normalization and Tokenization
        normalized_text = text_processor.normalize_text(query, detected_lang)
        st.markdown(f"**Normalized Text:** {normalized_text}")
        tokens = text_processor.process_text(query, detected_lang)
        st.markdown(f"**Tokens:** {', '.join(tokens['tokens'])}")
        tokens = tokens['tokens']
        # Step 3: Spelling Correction
        
        # This now loads JSON AND builds the n-gram index
        spell_corrector.load_json(detected_lang) 
        
        # 🎯 FIX 4: Correctly parse the dictionary returned by the spell corrector
        # get_confident_words_tokens returns a dict like: {'catured': [('captured', 0.8)]}
        correction_map = spell_corrector.get_confident_words_tokens(tokens)
        
        final_tokens = []
        for token in tokens:
            # Check if a correction exists AND the correction list is not empty
            if token in correction_map and correction_map[token]:
                # Get the top correction (word, score)
                top_correction_word = correction_map[token][0][0]
                final_tokens.append(top_correction_word)
            else:
                # No correction found, or list was empty, so keep the original token
                final_tokens.append(token)
                
        # Re-build the query string from the new list of tokens
        corrected_query = " ".join(final_tokens)
        
        # Display the corrected query
        if corrected_query != normalized_text:
            st.markdown(f"**Corrected Query:** {corrected_query}")
        else:
            st.markdown(f"**Corrected Query:** (No corrections needed)")
        
        
        # Step 4: Intent Detection
        # 🎯 FIX 5: Use the 'final_tokens' list, not the 'correction_map' dict
        intent_result = intent_detector.detect_intent(final_tokens, detected_lang)
        detected_kingdoms = intent_result['kingdoms']
        intent_confidence = intent_result['confidence']
        
        # Step 5: Query Expansion
        # Use the corrected_query string
        expansion_result = query_expander.expand_query(corrected_query, detected_lang, max_expansions=3)
        expanded_query = expansion_result['expanded_query']
        st.markdown(f"**Expanded Query:** {expanded_query}")
            
        # Step 6: Retrieval (using expanded query)
        retrieval_result = retrieval_system.search(
            expanded_query, detected_lang, detected_kingdoms
        )
            
        # Add expansion info to results
        retrieval_result['expansion_info'] = expansion_result
            
        # Display results
        display_results(query, lang_result, corrected_query, intent_result, retrieval_result)

def display_results(original_query, lang_result, corrected_query, intent_result, retrieval_result):
    """Display the processing results and retrieved information"""
    # Display main results
    if retrieval_result['paragraphs']:
        st.markdown("### Retrieved Information")
        
        for i, result in enumerate(retrieval_result['paragraphs'][:3]):  # Show top 3
            with st.container():
                st.markdown(f"**Result {i+1} (Similarity: {result['similarity']:.3f})**")
                st.markdown(f"**Kingdom:** {result['kingdom']}")
                st.markdown(f"**Language:** {result['language']}")
                st.write(result['text'])
                st.markdown("---")
    else:
        st.warning("No relevant information found. Try rephrasing your question.")
        
        # Suggestions
        st.markdown("### 💡 Try asking about:")
        st.markdown("""
        - Rulers and dynasties
        - Kingdom capitals and territories  
        - Historical events and wars
        - Architecture and culture
        - Time periods and dates
        """)

if __name__ == "__main__":
    main()