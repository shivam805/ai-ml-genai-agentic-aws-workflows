# Module 5: score the REVIEWER agent (Accuracy, Precision, Recall, F1)
# We give the reviewer reports we KNOW are good (3 sections) or bad (a section missing).
# YES class = APPROVED. A bad report that gets approved is the dangerous mistake.
# Run: python evaluate_reviewer.py

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from agents import reviewer_agent

GOOD = ("Summary: Data Science pays 85875, HR pays 62458.\n"
        "Top Domain: Data Science.\n"
        "Pay Gap: Data Science pays 23417 more than HR.")

TEST_REPORTS = [
    (GOOD, "APPROVED"),
    (GOOD.replace("Summary: Data Science pays", "Summary: Engineering pays"), "APPROVED"),
    (GOOD.replace("HR", "Marketing"), "APPROVED"),
    (GOOD + "\nTip: learn new skills.", "APPROVED"),
    ("Summary: Data Science pays 85875.\nTop Domain: Data Science.", "REJECTED"),   # no Pay Gap
    ("Top Domain: Data Science.\nPay Gap: 23417.", "REJECTED"),                      # no Summary
    ("Summary: Data Science pays 85875.\nPay Gap: 23417.", "REJECTED"),              # no Top Domain
    ("Salaries are different in every domain.", "REJECTED"),                         # nothing
]

real, predicted = [], []
for report, correct_answer in TEST_REPORTS:
    verdict = reviewer_agent(report)
    real.append(correct_answer)
    predicted.append("APPROVED" if verdict == "APPROVED" else "REJECTED")

print("Accuracy :", round(accuracy_score(real, predicted), 2))
print("Precision:", round(precision_score(real, predicted, pos_label="APPROVED", zero_division=0), 2))
print("Recall   :", round(recall_score(real, predicted, pos_label="APPROVED", zero_division=0), 2))
print("F1 score :", round(f1_score(real, predicted, pos_label="APPROVED", zero_division=0), 2))
