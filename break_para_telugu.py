import re
from pathlib import Path

CLEANED_INPUT = Path("cleaned_telugu_text.txt")
PARAGRAPH_OUTPUT = Path("paragraphs_4")

def split_telugu_sentences(text: str):
    """
    Splits Telugu text into sentences using regex on punctuation.
    Handles Telugu + English punctuation gracefully.
    """
    # Regex: split after sentence-ending punctuation followed by space
    sentences = re.split(r'(?<=[\.!?।])\s+', text)
    # Clean up empty entries
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences

def make_paragraphs(sentences, n=4):
    """
    Groups every n sentences into one paragraph.
    """
    paragraphs = [" ".join(sentences[i:i+n]) for i in range(0, len(sentences), n)]
    return paragraphs

if __name__ == "__main__":
    # 1️⃣ Read cleaned Telugu text
    text = CLEANED_INPUT.read_text(encoding="utf-8")
    
    # 2️⃣ Split into sentences
    sentences = split_telugu_sentences(text)
    print(f"Total Telugu sentences: {len(sentences)}")
    
    # 3️⃣ Group into paragraphs
    paragraphs = make_paragraphs(sentences, n=4)
    print(f"Total Telugu paragraphs: {len(paragraphs)}")
    
    # 4️⃣ Save to paragraphs_4 file
    with open(PARAGRAPH_OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n;;;\n".join(paragraphs))
    
    print(f"✅ Telugu paragraphs saved to: {PARAGRAPH_OUTPUT}")
