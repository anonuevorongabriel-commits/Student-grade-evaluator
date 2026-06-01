📘 Student Grade Evaluator App

📌 Application Description

The Student Grade Evaluator App is a standalone Python-based system designed to help students efficiently compute, monitor, and evaluate their academic performance. The application automates grade processing, removing the need for manual computation and reducing the risk of errors in calculating academic results such as the General Weighted Average (GWA).

The system follows a simple Input → Process → Output model, where users input subject grades, the program processes the data, and the system outputs a structured academic evaluation. It is designed as a lightweight offline application implemented in a single file (main.py), making it simple, portable, and easy to run without external dependencies aside from pytest for testing.

🎯 Core Features
1. Grade Evaluation

This feature allows users to input multiple subject grades. The system automatically computes the General Weighted Average (GWA) based on the provided data.

2. Goal Setter

Users can set a target GWA to serve as an academic performance goal. This helps students track and monitor their desired academic standing.

3. Goal Comparison

The system compares the computed GWA with the user-defined goal and determines whether the student meets or does not meet the target.

4. Academic Evaluation Output

The application generates a structured summary of academic performance, including:

Student name
Subject grades
Computed GWA
Target GWA
Final academic status

🧠 System Design Overview

The system is implemented in a single-file architecture (main.py), where all classes and functions are organized internally for simplicity and maintainability.

The design focuses on:

Clear separation of logic using classes
Easy readability for beginners
Minimal dependencies
Direct execution without complex setup

🧪 Testing Approach

Automated testing was implemented using pytest to ensure system reliability and correctness.

✔ Features Tested:

Student object initialization
Subject grade storage
GWA computation accuracy
Goal setting functionality
Goal comparison logic
Overall system behavior validation
▶ Run Tests:
py -m pytest -v

📁 Project Structure

Grade Evaluator App/


│
├── main.py
│   ├── Student Class
│   ├── GradeProcessor Class
│   ├── Grade computation logic
│   ├── Goal setting and comparison
│   └── Output display system
│
├── test_main.py
│   ├── Unit tests using pytest
│   ├── Student validation tests
│   ├── Grade computation tests
│   └── Goal evaluation tests
│
└── README.md
    └── Project documentation
▶ How to Run the Program
1. Run the application:
python main.py
2. Run automated tests:
py -m pytest -v

🧩 Technologies Used

Python 3.14
Object-Oriented Programming (OOP)
Pytest (Unit Testing Framework)
Single-file system architecture
Basic file execution environment

📊 System Workflow

User inputs student name and subject grades
System validates and stores data
GWA is computed automatically
User sets academic goal (optional)
System compares GWA with goal
Final evaluation is displayed

👨‍💻 Developer Note

This project was developed as an academic requirement to demonstrate understanding of programming fundamentals, object-oriented design, and automated testing using Python.

The system was designed to be simple, efficient, and beginner-friendly while still applying proper software development practices.

🧪 Testing Result

All automated test cases passed successfully using pytest, confirming that the system functions correctly and produces accurate academic evaluations.

📌 Summary

The Student Grade Evaluator App provides an efficient way for students to compute and track academic performance through automation. It demonstrates core programming principles including OOP, modular logic design, and unit testing, making it both an educational and functional system.

The Student Grade Evaluator App provides an efficient way for students to compute and track academic performance through automation. It demonstrates core programming principles including OOP, modular logic design, and unit testing, making it both an educational and functional system.
