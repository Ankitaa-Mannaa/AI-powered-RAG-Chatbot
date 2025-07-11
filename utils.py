import re
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def clean_text(raw_text):
    text = re.sub(r'\s+', ' ', raw_text)
    text = re.sub(r'Page \d+ of \d+', '', text)
    return text.strip()

import spacy
nlp = spacy.load("en_core_web_sm")

def chunk_sentences(text, min_words=100, max_words=300):
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents]
    
    chunks = []
    current_chunk = []
    words_in_chunk = 0

    for sentence in sentences:
        word_count = len(sentence.split())
        if words_in_chunk + word_count > max_words:
            if words_in_chunk >= min_words:
                chunks.append(" ".join(current_chunk))
                current_chunk = []
                words_in_chunk = 0
        current_chunk.append(sentence)
        words_in_chunk += word_count

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks


