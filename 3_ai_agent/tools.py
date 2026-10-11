# Module 3 - Tools: normal Python functions the agent can use.
# Each tool reads the salary data and returns a short text answer.

from pathlib import Path
import pandas as pd

df = pd.read_csv(Path(__file__).resolve().parent.parent / "data" / "employee_salaries.csv")


def get_employee_salary(name):
    rows = df[df["name"].str.lower().str.contains(name.lower())]
    if rows.empty:
        return f"No employee found with the name {name}."
    e = rows.iloc[0]
    return (f"{e['name']} works in {e['domain']} in {e['country']} with "
            f"{e['experience_years']} years of experience and earns {e['salary_usd']} USD per year.")


def get_domain_salary(domain):
    rows = df[df["domain"].str.lower() == domain.lower()]
    if rows.empty:
        return f"No data found for the domain {domain}."
    return f"Average salary in {domain}: {rows['salary_usd'].mean():.0f} USD per year."


def get_country_salary(country):
    rows = df[df["country"].str.lower() == country.lower()]
    if rows.empty:
        return f"No data found for the country {country}."
    return f"Average salary in {country}: {rows['salary_usd'].mean():.0f} USD per year."


def get_top_domain():
    averages = df.groupby("domain")["salary_usd"].mean().sort_values(ascending=False)
    return f"Highest paying domain: {averages.index[0]} ({averages.iloc[0]:.0f} USD per year)."


def compare_countries(country_one, country_two):
    one = df[df["country"].str.lower() == country_one.lower()]["salary_usd"].mean()
    two = df[df["country"].str.lower() == country_two.lower()]["salary_usd"].mean()
    return f"{country_one}: {one:.0f} USD, {country_two}: {two:.0f} USD, difference: {abs(one - two):.0f} USD."


def calculate_take_home(annual_salary, tax_percent):
    yearly = annual_salary * (1 - tax_percent / 100)
    return f"Take-home salary: {yearly:.0f} USD per year ({yearly / 12:.0f} USD per month)."


# A list of all tools. The agent finds a tool by its name.
TOOLS = {
    "get_employee_salary": get_employee_salary,
    "get_domain_salary": get_domain_salary,
    "get_country_salary": get_country_salary,
    "get_top_domain": get_top_domain,
    "compare_countries": compare_countries,
    "calculate_take_home": calculate_take_home,
}
