# Module 3: AI Agent (with a MOCK model - no paid AI needed)
#
# The agent loop:
#   1. THINK : ask the model what to do
#   2. ACT   : if the model wants a tool, run the tool
#   3. Give the tool result back to the model
#   4. Repeat until the model gives the final answer
#
# Run: python finance_agent.py

from tools import TOOLS
from mock_model import mock_model


def run_agent(question):
    """Returns (final_answer, list_of_tools_used)."""
    tool_results = []
    tools_used = []

    for round_number in range(1, 4):                    # maximum 3 rounds
        # 1. THINK
        decision = mock_model(question, tool_results)

        # 2. Final answer? Then we are done.
        if "answer" in decision:
            return decision["answer"], tools_used

        # 3. ACT: run the tool the model asked for
        name = decision["tool"]
        inputs = decision["inputs"]
        result = TOOLS[name](**inputs)
        print(f"   Round {round_number}: agent used tool '{name}' with {inputs}")
        tools_used.append(name)
        tool_results.append(result)

    return "Sorry, I could not finish.", tools_used


if __name__ == "__main__":
    print("Starting the salary agent (mock model)...")
    questions = [
        "How much does Priya earn?",
        "What is the average salary in Engineering?",
        "What is the average salary in Germany?",
        "Which domain pays the most?",
        "Compare the salary of India and USA.",
        "If my salary is 120000 and tax is 25 percent, what is my take-home?",
        "What does the word inflation mean?",
    ]
    for question in questions:
        print("\nQUESTION:", question)
        answer, tools_used = run_agent(question)
        print("ANSWER  :", answer)
