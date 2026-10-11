# Module 5: Agentic AI - the flow that connects the agents
# Goal: "Create a salary report"
#
#   Analyst -> Advisor -> Writer -> Reviewer
#                          ^__________|   (if rejected, the reviewer sends feedback back)
#
# Run: python flow.py

from pathlib import Path
import pandas as pd
from agents import analyst_agent, advisor_agent, writer_agent, reviewer_agent

# True  = the writer forgets a section in the 1st draft, so you can SEE the feedback loop
# False = the writer is perfect and the reviewer approves at once
SHOW_REJECTION_DEMO = True

print("Starting the agentic flow (mock agents)...")
print("GOAL: Create a salary report\n")

# Plain Python step: average salary of every domain, highest first
df = pd.read_csv(Path(__file__).resolve().parent.parent / "data" / "employee_salaries.csv")
domain_averages = df.groupby("domain")["salary_usd"].mean().round(0).sort_values(ascending=False)
print("Salary data:\n" + domain_averages.to_string() + "\n")

print("[1] Analyst agent is working...")
analysis = analyst_agent(domain_averages)
print(f"    Top: {analysis['top_name']}, lowest: {analysis['low_name']}, gap: {analysis['gap']:.0f} USD\n")

print("[2] Advisor agent is working...")
advice = advisor_agent(analysis)
print("    " + advice + "\n")

feedback = ""
for attempt in range(1, 4):                       # write -> review -> fix (maximum 3 times)
    print(f"[3] Writer agent, attempt {attempt}...")
    report = writer_agent(analysis, advice, feedback,
                          make_mistake=(SHOW_REJECTION_DEMO and attempt == 1))

    print("[4] Reviewer agent is checking...")
    verdict = reviewer_agent(report)
    print("    Reviewer says:", verdict, "\n")

    if verdict == "APPROVED":
        print("===== FINAL REPORT (approved) =====")
        print(report)
        break
    feedback = verdict                            # send the feedback back to the writer
else:
    print("Could not finish the goal in 3 attempts.")
