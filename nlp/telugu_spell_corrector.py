# telugu_counter.py

import json
import re
from collections import defaultdict

class TeluguWordCounter:
    def __init__(self, json_file):
        self.word_count = defaultdict(int)
        # Telugu Unicode range: U+0C00–U+0C7F
        self.telugu_pattern = re.compile(r"[\u0C00-\u0C7F]+(?:\.[\u0C00-\u0C7F]+)*")
        self._build_dict(json_file)
    
    def _build_dict(self, json_file):
        """Read the JSON and count Telugu words from each paragraph."""
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        for record in data.values():
            text = record.get("paragraph", "")
            words = self.telugu_pattern.findall(text)
            for word in words:
                self.word_count[word] += 1
    
    def check_word(self, word):
        """Return count of a specific word (0 if not found)."""
        return self.word_count.get(word, 0)
    
    def save_to_json(self, output_file):
        """Save the word counts to a JSON file."""
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(self.word_count, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    input_file = "labeled_paragraphs.json"
    output_file = "telugu_word_count.json"

    counter = TeluguWordCounter(input_file)
    counter.save_to_json(output_file)
    print(f"✅ Word counts saved to {output_file}")
