# Module 4: MCP Server
# MCP = Model Context Protocol: a standard way to give AI apps access to your tools.
# This file publishes 3 salary tools.
#
# You do NOT start this file yourself. client.py starts it automatically.
# (An MCP server talks through stdin/stdout, so it must not print anything.)

from mcp.server.fastmcp import FastMCP
import salary_logic

app = FastMCP("salary-server")


@app.tool()
def get_employee_salary(name: str) -> str:
    """Get the salary of one employee. Example name: Priya"""
    return salary_logic.employee_salary(name)


@app.tool()
def get_domain_salary(domain: str) -> str:
    """Get the average yearly salary of a domain. Example: Engineering"""
    return salary_logic.domain_salary(domain)


@app.tool()
def get_country_salary(country: str) -> str:
    """Get the average yearly salary of a country. Example: India"""
    return salary_logic.country_salary(country)


if __name__ == "__main__":
    app.run()
