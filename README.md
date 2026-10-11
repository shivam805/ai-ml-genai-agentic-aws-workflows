# Employee Salary AI Project (for beginners)

One company, **TechNova**, with 60 sample employees: name, domain, country, experience, salary.
The data is SAMPLE data for learning. Edit `data/employee_salaries.csv` to try your own numbers.
No paid AI model is needed: the "mock" parts are plain Python rules.

| # | Folder | Topic | Run (inside the folder) |
|---|--------|-------|-------------------------|
| 1 | 1_ml_model | Predict salary | `python ml_model.py` |
| 2 | 2_genai_rag | RAG: ingestion, then retrieval | `python create_docs.py`, `python ingestion_pipeline.py`, `python retrieval_pipeline.py` |
| 3 | 3_ai_agent | Agent with a mock model and tools | `python finance_agent.py` |
| 4 | 4_mcp | MCP server + client | `python client.py` (it starts the server for you) |
| 5 | 5_agentic_ai | 4 agents: analyst, advisor, writer, reviewer | `python flow.py` |

Scores (Accuracy, Precision, Recall, F1): module 1 prints them in `ml_model.py`.
Modules 2-5 have `evaluate_retrieval.py`, `evaluate_agent.py`, `evaluate_mcp.py`, `evaluate_reviewer.py`.

Setup (Python 3.10 or newer):

    python -m pip install -r requirements.txt

Later, with a real model: replace `mock_model()` (module 3) or the functions in `agents.py` (module 5)
with a call to your LLM. The rest of the code stays the same.
