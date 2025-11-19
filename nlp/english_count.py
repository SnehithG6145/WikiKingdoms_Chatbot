import json
import re
from collections import defaultdict

class EnglishWordCounter:
    def __init__(self, txt_file):
        """
        Initializes the counter, sets up the word count dictionary,
        defines the regex pattern for English words, and
        builds the dictionary from the input file.
        """
        self.word_count = defaultdict(int)
        # Regex to find words (sequences of letters)
        # \b ensures we capture whole words
        self.english_pattern = re.compile(r"\b[a-zA-Z]+\b")
        self._build_dict(txt_file)
    
    def _build_dict(self, txt_file):
        """
        Private method to read the text file and count the words.
        """
        try:
            # Open the text file
            with open(txt_file, "r", encoding="utf-8") as f:
                # Read the entire content
                text = f.read()
            
            # Find all words in the text
            words = self.english_pattern.findall(text)
            
            # Count each word, converting to lowercase for consistency
            for word in words:
                self.word_count[word.lower()] += 1
                
        except FileNotFoundError:
            print(f"Error: The file '{txt_file}' was not found.")
            # You might want to exit or raise the exception
            # raise
        except Exception as e:
            print(f"An error occurred: {e}")
            # raise

    def check_word(self, word):
        """
        Returns the count for a specific word (case-insensitive).
        """
        # Return the count for the specified word (case-insensitive)
        return self.word_count.get(word.lower(), 0)
    
    def save_to_json(self, output_file):
        """
        Saves the collected word counts to an output JSON file.
        """
        # Save the collected word counts to an output JSON file
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(self.word_count, f, ensure_ascii=False, indent=2)
        print(f"\nSuccessfully saved word counts to '{output_file}'")

# This block makes the script runnable from the command line
if __name__ == "__main__":
    # Define the input file (the one you provided)
    input_filename = "paragraphs_3.txt"
    
    # Define the name for the output JSON file
    output_filename = "english_word_counts.json"
    
    print(f"Processing '{input_filename}'...")
    
    # 1. Create an instance of the counter
    counter = EnglishWordCounter(input_filename)
    
    # 2. Save the results to a JSON file
    counter.save_to_json(output_filename)
    
    # 3. Example of how to check a specific word
    word_to_check = "dynasty"
    count = counter.check_word(word_to_check)
    print(f"The word '{word_to_check}' appears {count} times.")
    
    word_to_check = "kakatiya"
    count = counter.check_word(word_to_check)
    print(f"The word '{word_to_check}' appears {count} times.")