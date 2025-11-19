"""
Query expansion module to improve retrieval with synonyms and related terms
"""

class QueryExpander:
    """Expand queries with related terms, synonyms, and kingdom-specific vocabulary"""
    
    def __init__(self, gazetteer):
        self.gazetteer = gazetteer
        self.expansion_terms = self._build_expansion_dictionary()
    
    def _build_expansion_dictionary(self):
        """Build a dictionary of terms and their expansions"""
        expansion_dict = {}
        
        for kingdom, data in self.gazetteer.items():
            # Add primary names and their related terms
            for name in data.get('primary_names', []):
                name_lower = name.lower()
                if name_lower not in expansion_dict:
                    expansion_dict[name_lower] = set()
                
                # Add aliases as expansions
                expansion_dict[name_lower].update([a.lower() for a in data.get('aliases', [])])
                
                # Add rulers as related terms
                expansion_dict[name_lower].update([r.lower() for r in data.get('rulers', [])[:3]])
                
                # Add places as related terms
                expansion_dict[name_lower].update([p.lower() for p in data.get('places', [])[:2]])
            
            # Add rulers and their related terms
            for ruler in data.get('rulers', []):
                ruler_lower = ruler.lower()
                if ruler_lower not in expansion_dict:
                    expansion_dict[ruler_lower] = set()
                
                # Add kingdom name as expansion
                expansion_dict[ruler_lower].update([n.lower() for n in data.get('primary_names', [])[:2]])
                
                # Add capital/places
                expansion_dict[ruler_lower].update([p.lower() for p in data.get('places', [])[:1]])
        
        # Add general historical synonyms (English)
        general_expansions = {
            'king': ['ruler', 'monarch', 'emperor'],
            'kingdom': ['dynasty', 'empire', 'realm'],
            'capital': ['city', 'seat'],
            'war': ['battle', 'conflict', 'conquest'],
            'temple': ['shrine', 'monument'],
            'architecture': ['building', 'structure', 'construction'],
            'ruler': ['king', 'emperor', 'monarch'],
            'dynasty': ['kingdom', 'empire', 'lineage'],
            'empire': ['kingdom', 'realm', 'domain']
        }
        
        # Add Telugu general synonyms
        telugu_expansions = {
            'రాజు': ['పాలకుడు', 'చక్రవర్తి'],
            'రాజ్యం': ['వంశం', 'సామ్రాజ్యం'],
            'రాజధాని': ['నగరం'],
            'యుద్ధం': ['పోరాటం', 'సంగ్రామం'],
            'ఆలయం': ['దేవాలయం', 'గుడి'],
            'వాస్తుకళ': ['నిర్మాణం'],
            'పాలకుడు': ['రాజు', 'చక్రవర్తి'],
            'వంశం': ['రాజ్యం', 'సామ్రాజ్యం']
        }
        
        expansion_dict.update(general_expansions)
        expansion_dict.update(telugu_expansions)
        
        return expansion_dict
    
    def expand_query(self, query, language, max_expansions=3):
        """
        Expand query with related terms
        
        Args:
            query: original query string
            language: query language ('en' or 'te')
            max_expansions: maximum number of expansion terms to add
        
        Returns:
            dict with expanded query and expansion info
        """
        query_lower = query.lower()
        tokens = query_lower.split()
        
        expansion_terms = []
        expanded_tokens = set(tokens)
        
        # Find matching terms and their expansions
        for token in tokens:
            if token in self.expansion_terms:
                # Get expansions for this token
                expansions = list(self.expansion_terms[token])[:max_expansions]
                expansion_terms.extend(expansions)
                expanded_tokens.update(expansions)
        
        # Check for multi-word phrases in query
        for i in range(len(tokens)):
            for j in range(i+1, min(i+4, len(tokens)+1)):
                phrase = ' '.join(tokens[i:j])
                if phrase in self.expansion_terms:
                    expansions = list(self.expansion_terms[phrase])[:2]
                    expansion_terms.extend(expansions)
                    expanded_tokens.update(expansions)
        
        # Build expanded query
        expanded_query = query
        if expansion_terms:
            # Add expansion terms to the query
            unique_expansions = list(set(expansion_terms))[:max_expansions]
            expanded_query = query + ' ' + ' '.join(unique_expansions)
        
        return {
            'original_query': query,
            'expanded_query': expanded_query,
            'expansion_terms': list(set(expansion_terms)),
            'num_expansions': len(set(expansion_terms))
        }
    
    def get_related_terms(self, term, language, max_terms=5):
        """Get related terms for a specific term"""
        term_lower = term.lower()
        
        if term_lower in self.expansion_terms:
            related = list(self.expansion_terms[term_lower])[:max_terms]
            return related
        
        return []
    
    def expand_with_kingdom_context(self, query, detected_kingdoms, language):
        """
        Expand query using detected kingdom context
        
        Args:
            query: original query
            detected_kingdoms: list of detected kingdom names
            language: query language
        
        Returns:
            expanded query with kingdom-specific terms
        """
        expansion_terms = []
        
        # Add kingdom-specific terms
        for kingdom in detected_kingdoms:
            if kingdom in self.gazetteer:
                kingdom_data = self.gazetteer[kingdom]
                
                # Add key rulers
                rulers = kingdom_data.get('rulers', [])[:2]
                expansion_terms.extend([r.lower() for r in rulers])
                
                # Add key places
                places = kingdom_data.get('places', [])[:2]
                expansion_terms.extend([p.lower() for p in places])
        
        # Build expanded query
        expanded_query = query
        if expansion_terms:
            unique_terms = list(set(expansion_terms))[:3]
            expanded_query = query + ' ' + ' '.join(unique_terms)
        
        return {
            'original_query': query,
            'expanded_query': expanded_query,
            'kingdom_expansions': expansion_terms,
            'num_expansions': len(expansion_terms)
        }
    
    def get_expansion_stats(self):
        """Get statistics about the expansion dictionary"""
        return {
            'total_terms': len(self.expansion_terms),
            'avg_expansions': sum(len(v) for v in self.expansion_terms.values()) / len(self.expansion_terms) if self.expansion_terms else 0
        }
