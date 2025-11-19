import json
import os
import sys
import argparse
from typing import List, Dict
import pathlib

# Ensure project root is on sys.path so we can import local packages when run as a script
PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from data.gazetteer import get_gazetteer
from nlp.intent_detector import IntentDetector


def load_paragraphs(filepath: str) -> List[str]:
    """Load paragraphs from a text file. Splits on blank lines or the explicit ';;;' separator."""
    with open(filepath, 'r', encoding='utf-8') as f:
        raw = f.read()

    # Prefer explicit separator ';;;' if present
    if ';;;' in raw:
        parts = [p.strip() for p in raw.split(';;;')]
    else:
        # Split on two or more newlines
        parts = [p.strip() for p in raw.split('\n\n')]

    # Filter empty paragraphs
    paragraphs = [p for p in parts if p]
    return paragraphs


def simple_tokenize(text: str) -> List[str]:
    """Very small tokenizer: splits on whitespace and punctuation conservatively."""
    # Keep unicode letters; split on whitespace
    return [t for t in text.split() if t]


def label_paragraphs(paragraphs: List[str], detector: IntentDetector, language: str = 'auto') -> Dict[int, Dict]:
    """Run intent detector on each paragraph and return mapping of index->label info.

    Paragraphs with no confident kingdom intent are omitted (per user request).
    """
    labeled = {}

    for idx, para in enumerate(paragraphs):
        tokens = simple_tokenize(para)
        result = detector.detect_intent(tokens, language)

        kingdoms = result.get('kingdoms', [])
        confidence = result.get('confidence', 0.0)

        # Keep paragraph only if at least one kingdom detected
        if kingdoms:
            labeled[idx] = {
                'paragraph': para,
                'kingdoms': kingdoms,
                'confidence': confidence,
                'all_scores': result.get('all_scores', {})
            }

    return labeled


def main(argv=None):
    parser = argparse.ArgumentParser(description='Label paragraphs with kingdom intents')
    parser.add_argument('input', help='Input paragraphs file')
    parser.add_argument('--output', '-o', default='data/labeled_paragraphs.json', help='Output JSON file')
    parser.add_argument('--lang', '-l', default='auto', help='Language hint (not used by current detector)')

    args = parser.parse_args(argv)

    if not os.path.exists(args.input):
        print(f"Input file not found: {args.input}")
        sys.exit(2)

    paragraphs = load_paragraphs(args.input)

    gazetteer = get_gazetteer()
    detector = IntentDetector(gazetteer)

    labeled = label_paragraphs(paragraphs, detector, language=args.lang)

    # Ensure output directory exists
    out_dir = os.path.dirname(args.output)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(labeled, f, ensure_ascii=False, indent=2)

    print(f"Wrote {len(labeled)} labeled paragraphs to {args.output}")


if __name__ == '__main__':
    main()
