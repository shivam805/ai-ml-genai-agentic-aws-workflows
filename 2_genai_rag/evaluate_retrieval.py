# Module 2: score the retrieval (Accuracy, Precision, Recall, F1)
# For each question we know which document has the answer.
# We check the document of the BEST chunk the search found.
# Run after ingestion: python evaluate_retrieval.py

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from retrieval_pipeline import retrieve

TEST_QUESTIONS = [
    ("What is the average salary in Engineering?", "engineering.txt"),
    ("How many people are in Data Science?", "data_science.txt"),
    ("What is the average salary in Finance?", "finance.txt"),
    ("Who is the highest paid employee in HR?", "hr.txt"),
    ("How much do employees in Marketing earn?", "marketing.txt"),
    ("What is the average salary in India?", "india.txt"),
    ("How many people are in the USA?", "usa.txt"),
    ("Who is the highest paid employee in the UK?", "uk.txt"),
    ("What is the average salary in Germany?", "germany.txt"),
    ("How much do employees in Canada earn?", "canada.txt"),
    ("What is the difference between gross and take-home salary?", "salary_basics.txt"),
    ("Does salary grow with experience?", "salary_basics.txt"),
]

real_docs, found_docs = [], []
for question, correct_doc in TEST_QUESTIONS:
    best_source, _ = retrieve(question)[0]          # the top result
    real_docs.append(correct_doc)
    found_docs.append(best_source)

print("Accuracy :", round(accuracy_score(real_docs, found_docs), 2))
print("Precision:", round(precision_score(real_docs, found_docs, average="macro", zero_division=0), 2))
print("Recall   :", round(recall_score(real_docs, found_docs, average="macro", zero_division=0), 2))
print("F1 score :", round(f1_score(real_docs, found_docs, average="macro", zero_division=0), 2))
