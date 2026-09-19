# Daily Expense Tracker 🎓🚀

A robust, command-line Expense Tracker built in Python to manage expense records, calculate automated spending, generate sorted performance reports, and handle custom exceptions gracefully.

---

## 📁 Project Structure

Daily-Expense-Tracker/
│
├──config/
│   └── sql_connect.py          # Configuration settings (file paths, constants)
|
├── data/
│   └── database.py         # Persistent storage for expense records
│
├── src/
│   ├── __init__.py            # Package initialization & import gateway
│   ├── tracker.py             # Core business logic (add, calculate, format)
│   └── utils.py               # Custom exceptions & input validation rules
│
├── main.py                    # Application entry point (Streamlit app)
└── README.md                  # Project documentation

---

## ✨ Features

* __Dynamic Record Management:__ Add multiple expenses along with their respective details.

---

## ⚙️ Prerequisites

* Python 3.8 or higher installed on your system.

---

## 🚀 How to Run

1. Clone or open the project folder in your terminal.
2. Ensure your directory structure matches above, with an empty or properly formatted data/students.json file.
3. Run the main application file:

```bash
python main.py
