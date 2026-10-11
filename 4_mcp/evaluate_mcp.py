# Module 4: score the tool get_domain_salary (Accuracy, Precision, Recall, F1)
# Does the tool FIND real domains and say "not found" for fake ones?
# YES class = "found". No server is needed (we call the same function the server uses).
# Run: python evaluate_mcp.py

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import salary_logic

# (domain name, does it really exist in the data?)
TEST_DOMAINS = [
    ("Engineering", True), ("Data Science", True), ("Finance", True), ("HR", True),
    ("Marketing", True), ("engineering", True), ("hr", True),
    ("Sales", False), ("Legal", False), ("", False), ("Enginering", False), ("Cooking", False),
]

real, predicted = [], []
for domain, exists in TEST_DOMAINS:
    answer = salary_logic.domain_salary(domain)
    real.append("found" if exists else "not found")
    predicted.append("not found" if "not found" in answer else "found")

print("Accuracy :", round(accuracy_score(real, predicted), 2))
print("Precision:", round(precision_score(real, predicted, pos_label="found"), 2))
print("Recall   :", round(recall_score(real, predicted, pos_label="found"), 2))
print("F1 score :", round(f1_score(real, predicted, pos_label="found"), 2))
