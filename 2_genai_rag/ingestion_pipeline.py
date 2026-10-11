# Module 2 - Flow 1: DATA INGESTION
# Documents -> Chunks -> Vectors -> Saved index
# Run once: python ingestion_pipeline.py
#
# We use TF-IDF (from scikit-learn) to turn text into numbers.
# It is free, runs on your computer and needs no internet or API key.

from pathlib import Path
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

folder = Path(__file__).resolve().parent
LINES_PER_CHUNK = 1          # one chunk = 1 line (one short fact) of a document

# Step 1: read every .txt file
documents = {}
for file in sorted((folder / "docs").glob("*.txt")):
    documents[file.name] = file.read_text().splitlines()
print("Step 1: loaded", len(documents), "documents")

# Step 2: cut every document into small chunks
chunks = []        # the text of each chunk
sources = []       # the file name of each chunk
for file_name, lines in documents.items():
    for start in range(0, len(lines), LINES_PER_CHUNK):
        chunks.append("\n".join(lines[start:start + LINES_PER_CHUNK]))
        sources.append(file_name)
print("Step 2: created", len(chunks), "chunks")

# Step 3: turn the chunks into numbers (vectors) and save them
vectorizer = TfidfVectorizer(stop_words="english")   # ignore common words like "the", "in", "how"
vectors = vectorizer.fit_transform(chunks)
joblib.dump({"vectorizer": vectorizer, "vectors": vectors,
             "chunks": chunks, "sources": sources}, folder / "index.joblib")
print("Step 3: saved the index in index.joblib")
print("Ingestion finished!")
