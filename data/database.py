import sys
from pathlib import Path
import pandas as pd  # type:ignore
from sqlalchemy import text  # type: ignore

# Locate the project root and add it to Python's module search path.
current_dir = Path(__file__).resolve()
for parent in [current_dir] + list(current_dir.parents):
    if parent.name == "Daily-Expense-Tracker":
        sys.path.append(str(parent))
        break

# Import the database engine from the project configuration.
# # fmt: off
from config.sql_connect import engine # type:ignore
# # fmt: on

# ==============================================================
# Database setup helpers
# ==============================================================


def use_db():
    """Select the expense tracker database for the current connection."""
    use_db = 'USE expense_tracker ;'
    with engine.connect() as connection:
        connection.exec_driver_sql(use_db)


def create_table():
    """Create the expenses table if it does not already exist."""
    create_table_sql = '''
      CREATE TABLE IF NOT EXISTS expense (
      id INT PRIMARY KEY AUTO_INCREMENT,
      expense_name VARCHAR(255) NOT NULL,
      expense_date DATE DEFAULT (CURRENT_DATE),
      payment_type VARCHAR(20) DEFAULT 'CASH' CHECK (payment_type IN ('CASH', 'UPI'))
  );
  '''
    with engine.connect() as connection:
        connection.exec_driver_sql(create_table_sql)


def get_expense():
    """Fetches all expense records from the database as a Pandas DataFrame."""
    query = "SELECT * FROM expense;"
    df = pd.read_sql(query, con=engine)
    return df
