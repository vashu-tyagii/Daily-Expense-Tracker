# Student Grade Tracker 🎓🚀

A robust, command-line Student Grade Tracker built in Python to manage student records, calculate automated grades, generate sorted performance reports, and handle custom exceptions gracefully.

---

## 📁 Project Structure

Student-Grade-Tracker/
│
├── data/
│   └── students.json        # Persistent storage for student records
│
├── src/
│   ├── __init__.py            # Package initialization & import gateway
│   ├── tracker.py             # Core business logic (add, calculate, format)
│   └── utils.py               # Custom exceptions & input validation rules
│
├── main.py                    # Application entry point (CLI loop)
└── README.md                  # Project documentation

---

## ✨ Features

* __Dynamic Record Management:__ Add multiple students along with their respective marks lists.
* __Automated Grading System:__ Calculates student averages and assigns letter grades (A, B, C, F) using strict conditional logic.
* __Sorted Performance Reports:__ Automatically generates and prints a clean report sorted by highest average first.
* __Robust Error Handling:__ Custom exception handling (EmptyMarksError) to prevent crashes on empty inputs or invalid data types.

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
