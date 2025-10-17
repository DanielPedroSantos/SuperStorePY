Short, focused instructions to help an AI assistant contribute to the SuperStorePY project.

Repository snapshot
- Python project for SuperStore data processing and dimensional modeling. Key files:
  - `acessobanco.py` — creates a SQLAlchemy engine using environment variables (DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME).
  - `Dataset/Sample - Superstore.xlsx` — canonical sample data used in notebooks.
  - Notebooks (`*.ipynb`, e.g., `Dim_Cliente.ipynb`, `Analise_Exploratoria.ipynb`) — primary exploratory and ETL draft code. Treat notebooks as source-of-truth for analysis flow.
  - `Bancos/acessobanco.env` — example environment file; production secrets are not stored in repo.

What to change and how
- When modifying database access, update `acessobanco.py` only. It centralizes DB connection creation using `create_engine` and dotenv. Follow its pattern: read env vars with `os.getenv`, call `create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}")`.
- Keep notebooks small, prefer extracting reusable logic into `.py` modules (e.g., `utils/`) when code is reused across notebooks.

Coding conventions & patterns
- Lightweight script style: modules and notebooks use direct top-level code for quick ETL proofs. When converting to production, wrap logic into functions with clear inputs/outputs (pandas DataFrame in, DataFrame or DB writes out).
- DB operations: prefer SQLAlchemy engines from `acessobanco.acessobanco()` and use `pandas.to_sql` or `engine.connect().execute(text(...))` for SQL snippets.
- Environment: rely on `.env` variables loaded via `dotenv.load_dotenv()`; do not hard-code credentials. Reference `Bancos/acessobanco.env` as the example.

Examples and patterns in this repo
- Opening a DB engine (from `acessobanco.py`):
  - Use `from acessobanco import acessobanco` and then `engine = acessobanco()`.
- Notebook imports (example from `Dim_Cliente.ipynb`):
  - `import pandas as pd`
  - `from sqlalchemy import text, create_engine`
  - `from dotenv import load_dotenv`
  - `from acessobanco import acessobanco`

Testing, running and debugging
- There is no test harness in repo; run notebooks interactively. For quick smoke runs:
  - Create a `.env` (copy `Bancos/acessobanco.env`) and export the variables, or place the file in project root and rely on `load_dotenv()`.
  - Run small scripts with `python3 script.py` (e.g., `python3 teste1.py`).
- When making changes to DB code, test against a development DB; do not assume production credentials.

What not to do
- Do not add credentials or large binary datasets to the repo.
- Avoid editing notebooks in ways that break their narrative cells; prefer moving logic to `.py` files and keeping notebooks for exposition.

Where to look next
- `acessobanco.py` — DB connection pattern
- `Dataset/Sample - Superstore.xlsx` — canonical dataset
- Notebooks (`Dim_Cliente.ipynb`, `Analise_Exploratoria.ipynb`) — show ETL intent and examples to port to scripts

If unclear
- Ask which environment (local dev vs staging) to target for DB runs and whether you should extract notebook code into a reusable module.

Feedback request: tell me if you'd like stricter rules (formatting, linting, tests) or if I should merge any existing README content into this file.
