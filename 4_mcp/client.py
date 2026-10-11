# Module 4: MCP Client
# Run only this file (it starts server.py for you):  python client.py

import asyncio
import sys
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# How to start the server: "python server.py"
server = StdioServerParameters(command=sys.executable,
                               args=[str(Path(__file__).resolve().parent / "server.py")])


async def main():
    print("Starting the MCP server and connecting...")
    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("Connected!\n")

            # 1. Ask the server which tools it has
            tools = await session.list_tools()
            print("Tools on the server:")
            for tool in tools.tools:
                print(" -", tool.name, ":", tool.description)

            # 2. Call the tools
            calls = [("get_employee_salary", {"name": "Priya"}),
                     ("get_domain_salary", {"domain": "Engineering"}),
                     ("get_country_salary", {"country": "Germany"})]
            for name, arguments in calls:
                result = await session.call_tool(name, arguments)
                print(f"\nTool {name} {arguments}")
                print("Result:", result.content[0].text)


try:
    asyncio.run(main())
except Exception as error:
    print("ERROR:", error)
    print("Did you run: python -m pip install -r requirements.txt ?")
