from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, text

# SQLite database file path (project directory ke andar expenses.db banayega)
DB_PATH = Path(__file__).resolve().parent.parent / "expenses.db"

# SQLAlchemy engine setup for SQLite
engine = create_engine(f"sqlite:///{DB_PATH}", echo=True)


def init_db():
    """Creates the expense table automatically if it doesn't exist."""
    with engine.connect() as conn:
        conn.execute(
            text("""
            CREATE TABLE IF NOT EXISTS expense (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                expense_name TEXT NOT NULL,
                expense_date TEXT DEFAULT CURRENT_DATE,
                payment_type TEXT DEFAULT 'CASH',
                expense_amount REAL NOT NULL
            );
        """)
        )
        conn.commit()


def get_expense():
    """Fetches all expense records as a Pandas DataFrame."""
    init_db()  # Har baar query chalane se pehle ensure karo ki table bani ho
    query = "SELECT * FROM expense"
    df = pd.read_sql(query, con=engine)
    return df


# App start hote hi table initialize kar do
init_db()
