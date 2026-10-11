# Plain Python salary functions. The MCP server (server.py) calls these.

from pathlib import Path
import pandas as pd

df = pd.read_csv(Path(__file__).resolve().parent.parent / "data" / "employee_salaries.csv")


def employee_salary(name):
    rows = df[df["name"].str.lower().str.contains(name.lower())] if name.strip() else df.iloc[0:0]
    if rows.empty:
        return f"Employee {name} not found."
    e = rows.iloc[0]
    return f"{e['name']} ({e['domain']}, {e['country']}) earns {e['salary_usd']} USD per year."


def domain_salary(domain):
    rows = df[df["domain"].str.lower() == domain.lower()]
    if rows.empty:
        return f"Domain {domain} not found."
    return f"{rows['domain'].iloc[0]}: average salary {rows['salary_usd'].mean():.0f} USD per year ({len(rows)} employees)."


def country_salary(country):
    rows = df[df["country"].str.lower() == country.lower()]
    if rows.empty:
        return f"Country {country} not found."
    return f"{rows['country'].iloc[0]}: average salary {rows['salary_usd'].mean():.0f} USD per year ({len(rows)} employees)."
