# Module 2 - Flow 2: DATA RETRIEVAL (RAG)
# Question -> find the best chunks -> MOCK model writes the answer
# Run after ingestion: python retrieval_pipeline.py
#
# No real AI model is used. The "mock LLM" just returns the best chunk.

from pathlib import Path
import joblib
from sklearn.metrics.pairwise import cosine_similarity

index_file = Path(__file__).resolve().parent / "index.joblib"
if not index_file.exists():
    raise SystemExit("index.joblib not found. Run these first:  python create_docs.py  then  python ingestion_pipeline.py")
index = joblib.load(index_file)


def retrieve(question, top_k=2):
    """Return the top_k most similar chunks as (source, text) pairs."""
    question_vector = index["vectorizer"].transform([question])
    scores = cosine_similarity(question_vector, index["vectors"])[0]
    best = scores.argsort()[::-1][:top_k]                  # biggest scores first
    return [(index["sources"][i], index["chunks"][i]) for i in best]


def mock_llm(question, chunks):
    """Pretend to be an LLM: just return the best chunk.
    A real LLM would read all chunks and write a nicer sentence."""
    best_chunk_text = chunks[0][1]
    return best_chunk_text


def ask(question):
    print("\nQuestion:", question)
    chunks = retrieve(question)
    print("Retrieved chunks:")
    for source, text in chunks:
        print("  -", source, "|", text)
    print("Answer:", mock_llm(question, chunks))


if __name__ == "__main__":
    print("Starting retrieval...")
    ask("What is the average salary in Engineering?")
    ask("How much do employees in Germany earn?")
    ask("Who is the highest paid employee in the USA?")
    ask("What is the difference between gross and take-home salary?")
