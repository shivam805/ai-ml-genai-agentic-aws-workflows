# Module 3 - The MOCK model (a fake "brain", no AI and no internet needed)
#
# A real LLM reads the question and decides: "use this tool" or "here is the answer".
# This mock does the same job with simple if-rules and keywords.
# Later you can replace mock_model() with a real LLM call.

from tools import df

# Words the mock model knows, taken from the data
KNOWN_DOMAINS = sorted(df["domain"].unique())
KNOWN_COUNTRIES = sorted(df["country"].unique())
KNOWN_FIRST_NAMES = [name.split()[0] for name in df["name"]]


def find_words(question, known_words):
    """Return the known words that appear in the question."""
    text = question.lower().replace("?", " ").replace(",", " ").replace(".", " ")
    return [word for word in known_words if f" {word.lower()} " in f" {text} "]


def mock_model(question, tool_results):
    """Return {"tool": name, "inputs": {...}} or {"answer": text}."""

    # The tool already ran -> time to give the final answer
    if tool_results:
        return {"answer": tool_results[-1]}

    q = question.lower()
    countries = find_words(question, KNOWN_COUNTRIES)
    domains = find_words(question, KNOWN_DOMAINS)
    people = find_words(question, KNOWN_FIRST_NAMES)
    numbers = [float(w) for w in q.replace("?", " ").replace(",", " ").split() if w.replace(".", "").isdigit()]

    if ("take-home" in q or "take home" in q) and len(numbers) >= 2:
        return {"tool": "calculate_take_home",
                "inputs": {"annual_salary": numbers[0], "tax_percent": numbers[1]}}
    if len(countries) == 2:
        return {"tool": "compare_countries",
                "inputs": {"country_one": countries[0], "country_two": countries[1]}}
    if people:
        return {"tool": "get_employee_salary", "inputs": {"name": people[0]}}
    if domains:
        return {"tool": "get_domain_salary", "inputs": {"domain": domains[0]}}
    if countries:
        return {"tool": "get_country_salary", "inputs": {"country": countries[0]}}
    if "domain" in q and ("highest" in q or "most" in q or "top" in q):
        return {"tool": "get_top_domain", "inputs": {}}

    return {"answer": "Sorry, I can only answer questions about employee, domain and country salaries."}
