# Module 3: score the agent's TOOL CHOICE (Accuracy, Precision, Recall, F1)
# For each question we know which tool the agent SHOULD use ("none" = no tool needed).
# Run: python evaluate_agent.py

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from finance_agent import run_agent

TEST_QUESTIONS = [
    ("How much does Emily earn?", "get_employee_salary"),
    ("What is the salary of Lukas?", "get_employee_salary"),
    ("What is the average salary in Finance?", "get_domain_salary"),
    ("How much do people earn in Data Science?", "get_domain_salary"),
    ("What is the average salary in the UK?", "get_country_salary"),
    ("How much do employees in Canada earn?", "get_country_salary"),
    ("Which domain pays the most?", "get_top_domain"),
    ("Which domain has the highest salary?", "get_top_domain"),
    ("Compare the salary of Germany and India.", "compare_countries"),
    ("Who pays more, USA or UK?", "compare_countries"),
    ("Take-home pay for 90000 salary with 20 percent tax?", "calculate_take_home"),
    ("Monthly take-home for 150000 with 30 percent tax?", "calculate_take_home"),
    ("What does the word inflation mean?", "none"),
    ("Why is it good to save money?", "none"),
]

real_tools, chosen_tools = [], []
for question, correct_tool in TEST_QUESTIONS:
    _, tools_used = run_agent(question)
    real_tools.append(correct_tool)
    chosen_tools.append(tools_used[0] if tools_used else "none")      # first tool used

print("\nAccuracy :", round(accuracy_score(real_tools, chosen_tools), 2))
print("Precision:", round(precision_score(real_tools, chosen_tools, average="macro", zero_division=0), 2))
print("Recall   :", round(recall_score(real_tools, chosen_tools, average="macro", zero_division=0), 2))
print("F1 score :", round(f1_score(real_tools, chosen_tools, average="macro", zero_division=0), 2))
