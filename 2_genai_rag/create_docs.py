# Creates small text documents from the salary data (run once: python create_docs.py)
# One document per domain, one per country, and one general document.
# Every line is a short fact that can be found on its own.

from pathlib import Path
import pandas as pd

folder = Path(__file__).resolve().parent
df = pd.read_csv(folder.parent / "data" / "employee_salaries.csv")
(folder / "docs").mkdir(exist_ok=True)


def write_document(group_column):
    for value, rows in df.groupby(group_column):
        top = rows.loc[rows["salary_usd"].idxmax()]
        lines = [
            f"Employees in {value} earn an average salary of {rows['salary_usd'].mean():.0f} USD per year.",
            f"{value} has {len(rows)} people in the team.",
            f"The highest paid employee in {value} is {top['name']} with {top['salary_usd']} USD.",
        ]
        file_name = value.lower().replace(" ", "_") + ".txt"
        (folder / "docs" / file_name).write_text("\n".join(lines))


write_document("domain")
write_document("country")

(folder / "docs" / "salary_basics.txt").write_text(
    "Salary basics.\n"
    "Gross salary is the full yearly pay before tax. Take-home salary is what you get after tax.\n"
    "For example, with a gross salary of 100000 and tax of 20 percent, the take-home is 80000.\n"
    "Salary usually grows with years of experience."
)
print("Created documents:", sorted(p.name for p in (folder / "docs").glob("*.txt")))
