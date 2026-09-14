# Python Foundation — 10 Practical Mini-Projects

(No toy math problems — real, usable programs combining everything you've learned)

Rule: Build each one as a complete, runnable script. Use functions, proper
error handling, and file I/O wherever it makes sense — don't just write
one-off code, structure it like a real small tool.

---

## 1. Student Grade Tracker

Build a program that:

- Stores students as a list of dictionaries: {"name": ..., "marks": [...]}
- Has a function to add a new student
- Has a function to calculate each student's average and assign a grade
  (A/B/C/F) using conditionals
- Prints a formatted report of all students, sorted by average (highest first)
- Handles the case where marks list is empty (exception handling)

---

## 2. Personal Expense Tracker (File-Based)

Build a program that:

- Lets the user add an expense (category, amount, date) via input()
- Saves each expense as a line in a CSV/text file (append mode)
- Has a function to read the file and show total spending per category
  (use a dictionary to accumulate totals)
- Has a function to show the top 3 highest expenses
- Handles the case where the file doesn't exist yet (exception handling)

---

## 3. Contact Book (CRUD with a Dictionary)

Build a program that:

- Stores contacts as a dictionary: {name: {"phone": ..., "email": ...}}
- Functions to: add contact, update contact, delete contact, search contact
- Saves/loads contacts to/from a text file so data persists between runs
- Validates that phone numbers are digits only before saving (exception handling)

---

## 4. Word Frequency Analyzer (From a Text File)

Build a program that:

- Reads any text file (a paragraph you paste in)
- Counts frequency of each word using a dictionary
- Uses `filter()` to remove common words (the, is, a, and, etc.) — build
  your own small "stopword" list
- Uses `sorted()` with a lambda to print the top 5 most frequent words
- Handles a missing file gracefully (exception handling)

---

## 5. Simple Inventory Management System

Build a program that:

- Stores products as a list of dictionaries (name, quantity, price)
- Function to add stock, function to sell/remove stock (with a check that
  quantity never goes negative — raise a custom exception if it would)
- Uses `map()` to calculate the total value of each product (qty × price)
- Uses `filter()` to show products that are low on stock (below a threshold)
- Prints a summary report of total inventory value

---

## 6. Employee Bonus Calculator (*args and **kwargs practice)

Build a program that:

- A function `calculate_bonus(base_salary, *performance_scores, **extras)`
  that: averages the performance scores, applies a bonus % based on average
  score (using conditionals), and adds any extra bonuses passed via kwargs
  (like festival_bonus=2000)
- Test it with multiple employees, each with different numbers of scores
  and different extra bonuses
- Print a clean summary for each employee

---

## 7. Duplicate File/Entry Finder

Build a program that:

- Given a list of "records" (e.g., email addresses or student IDs from a
  file), find and report duplicates
- Uses a set to identify which entries are unique vs repeated
- Uses a dictionary to count exactly how many times each duplicate appears
- Writes the duplicate report to a new output file

---

## 8. Simple Data Validator (For a CSV-like Dataset)

Build a program that:

- Takes a list of dictionaries representing rows of data (e.g., students
  with name, age, email)
- Validates each row: age must be a number and between 5-100, email must
  contain "@", name must not be empty
- Uses exception handling to catch bad rows without crashing the whole program
- Separates valid and invalid rows into two lists, and writes both to
  separate output files

---

## 9. Sales Report Generator (Filter + Map + Reduce Combined)

Build a program that:

- Given a list of sales records (dictionaries: product, amount, region)
- Uses `filter()` to get sales only from one region
- Uses `map()` to apply a 10% tax to each sale amount
- Uses `reduce()` (from functools) to get the total taxed revenue for
  that region
- Prints a formatted summary — do this for at least 2 different regions

---

## 10. Login System with Attempt Limiting

Build a program that:

- Stores usernames and passwords in a dictionary (or a file)
- Function to check login — if password is wrong, raise a custom exception
  and track failed attempts
- After 3 failed attempts for a username, lock them out (print a message,
  don't allow further tries in that session)
- Log every login attempt (success or failure) with a timestamp to a text file

---

## Self-Check

For each project, before moving to the next:

- [ ] Does it run without crashing on bad input (empty file, wrong type, etc.)?
- [ ] Did you use at least one function with proper parameters/return?
- [ ] Did you handle at least one error case with try/except instead of
      letting the program crash?

These 10, done properly, are genuinely more useful for interviews than
textbook math problems — each one mirrors a small real-world tool.
