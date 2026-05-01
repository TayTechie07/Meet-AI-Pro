from transformers import pipeline
from sentence_transformers import SentenceTransformer

# Hugging Face models
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

embedder = SentenceTransformer("all-MiniLM-L6-v2")