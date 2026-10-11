# Module 5: the 4 agents (MOCK - no AI model needed)
# Every agent is a small Python function with ONE job.
# In a real project each function would call an LLM with a different role.


def analyst_agent(domain_averages):
    """Job: rank the domains by average salary and find the pay gap."""
    ranking = list(domain_averages.items())            # already sorted: highest first
    top_name, top_salary = ranking[0]
    low_name, low_salary = ranking[-1]
    return {"ranking": ranking,
            "top_name": top_name, "top_salary": top_salary,
            "low_name": low_name, "low_salary": low_salary,
            "gap": top_salary - low_salary}


def advisor_agent(analysis):
    """Job: give simple advice based on the analysis.
    (The sentences are fixed text. A real LLM would write its own advice.)"""
    return (f"Advice: {analysis['top_name']} pays the most because its skills are in high demand. "
            f"{analysis['low_name']} pays the least. "
            f"Tip: learn skills from {analysis['top_name']} to grow your salary.")


def writer_agent(analysis, advice, feedback, make_mistake=False):
    """Job: write the report with 3 sections: Summary, Top Domain, Pay Gap."""
    ranking_text = ", ".join(f"{name} {salary:.0f}" for name, salary in analysis["ranking"])
    sections = [
        f"Summary: average salary by domain (USD): {ranking_text}.",
        f"Top Domain: {analysis['top_name']} pays the most ({analysis['top_salary']:.0f} USD).",
        f"Pay Gap: {analysis['top_name']} pays {analysis['gap']:.0f} USD more than {analysis['low_name']}.",
    ]
    if make_mistake:                  # demo only: the writer "forgets" the last section
        sections = sections[:2]
    return "\n".join(sections) + "\n" + advice


def reviewer_agent(report):
    """Job: check that the report has all 3 sections."""
    missing = [section for section in ["Summary", "Top Domain", "Pay Gap"]
               if section + ":" not in report]
    if missing:
        return "REJECTED: missing " + ", ".join(missing)
    return "APPROVED"
