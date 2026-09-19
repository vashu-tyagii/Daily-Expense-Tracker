import sys
from pathlib import Path

# Automatic root folder dhoondhne wala loop
current_dir = Path(__file__).resolve()
for parent in [current_dir] + list(current_dir.parents):
  if parent.name == "Daily-Expense-Tracker":
    sys.path.append(str(parent))
    break

# # fmt: off
from config.sql_connect import engine  # type: ignore
# # fmt: on

