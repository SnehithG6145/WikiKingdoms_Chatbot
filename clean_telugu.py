import re
import unicodedata
from pathlib import Path

INPUT = Path("Telugu_scrapped_text.txt")
CLEAN_OUT = Path("cleaned_telugu_text.txt")

def clean_telugu_text(text: str) -> str:
    # 1. Normalize Unicode (important for Telugu diacritics)
    text = unicodedata.normalize("NFC", text)
    
    # 2. Remove URLs
    text = re.sub(r"https?://\S+", " ", text)
    
    # 3. Remove English or Wiki-style headings like "== History =="
    text = re.sub(r"={2,}.*?={2,}", " ", text)
    
    # 4. Remove common Wiki UI artifacts or boilerplate Telugu text
    text = re.sub(
        r"(This box:|viewtalkedit|ప్రారంభ|చివర|వ్యాసం|చర్చ|చదువు|సవరించు|వికీపీడియా నుండి)",
        " ",
        text,
        flags=re.I
    )
    
    # 5. Remove citations like [1], [12,34]
    text = re.sub(r"\[\s*\d+(?:\s*,\s*\d+)*\s*\]", " ", text)
    
    # 6. Remove stray HTML tags
    text = re.sub(r"<[^>]+>", " ", text)
    
    # 7. Remove unwanted characters but **keep Telugu + sentence punctuation**
    text = re.sub(r"[^\u0C00-\u0C7F\s\.！？!?।]+", " ", text)
    
    # 8. Collapse multiple spaces into one
    text = re.sub(r"\s+", " ", text).strip()
    
    return text

# --- Usage ---
if __name__ == "__main__":
    raw_text = INPUT.read_text(encoding="utf-8")
    cleaned_text = clean_telugu_text(raw_text)
    CLEAN_OUT.write_text(cleaned_text, encoding="utf-8")
    print("✅ Cleaned Telugu text saved to:", CLEAN_OUT)
