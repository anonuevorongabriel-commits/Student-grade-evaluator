Student Grade Evaluator App

Application Description

The Student Grade Evaluator App is a standalone Python application developed using a single-file structure to help students efficiently compute, monitor, and evaluate their academic performance. The system automates grade processing tasks that are often done manually, reducing calculation errors and improving the speed and accuracy of academic evaluation.

The application follows an Input → Process → Output model where users input grades, the system processes academic data, and structured evaluation results are generated automatically. The application was designed as a lightweight offline system that requires no internet connection or external database.



Core Features

1.	Grade Evaluation
This feature allows users to input subject grades and automatically computes the General Weighted Average (GWA). The system evaluates whether the student passes or fails based on predefined academic criteria.

2.	Goal Setter
This feature enables users to define a target GWA that they want to achieve academically. The target serves as a reference point for academic monitoring.

3.	Goal Comparison
The application compares the student’s computed GWA against the target GWA and determines whether academic goals were achieved.

4.	Academic Evaluation Output
The system generates organized outputs displaying subject grades, computed GWA, target GWA, and academic standing.





System Design Rationale

The application was intentionally designed to remain simple and easy to use while demonstrating programming concepts and problem-solving techniques.

The modular design is implemented within a single file (main.py), where classes and functions are organized internally to separate processing logic, student information handling, and evaluation methods. This approach improves readability, maintainability, and scalability while still using a single-file architecture.

The offline design ensures accessibility and usability regardless of internet availability, making it suitable for students in various learning environments.



OOP Concepts Used

Encapsulation
Encapsulation is implemented by grouping student information such as grades, subjects, target GWA, and academic status inside the Student class.

Abstraction
Abstraction is applied through the GradeProcessor class where computation logic is hidden from the user.

Inheritance
Inheritance is demonstrated through structured class organization where common behaviors can be reused or extended.

Polymorphism
Polymorphism is applied through methods that process different grade datasets while maintaining consistent evaluation behavior.

Modularity
The project follows modular programming practices inside a single file by separating responsibilities into classes and functions.



Technologies Used

• Python – Primary programming language
• Pytest – Automated testing framework
• Object-Oriented Programming Principles
• File Handling Operations
• Core Programming Logic
• Offline Execution Environment



System Workflow

1.	User inputs student information and subject grades
2.	System validates entered data
3.	Grades are processed and GWA is computed
4.	Goal GWA is compared with computed results
5.	Academic evaluation results are displayed
6.	User reviews generated evaluation output

How to Run the System

1.	Requirements
• Python 3.x installed

2.	Run Program

Python main.py


Running Tests

Command Used:
Py -m pytest -v


Pytest Validation Coverage

The automated tests verified:

• Student object initialization
• Subject grade storage
• GWA computation accuracy
• Pass/Fail evaluation
• Goal setter functionality
• Goal comparison logic
• Invalid input handling
• Empty subject handling
• Output generation consistency

Figure XX: Pytest Execution Results

The pytest execution results show that all test cases passed successfully without failures or errors. This confirms that the Student Grade Evaluator App performs computations correctly, processes student data accurately, and handles expected and edge-case inputs properly.

Successful execution of all automated tests indicates that the application is reliable, functionally stable, and capable of producing consistent academic evaluation results.



Author

Developed by:

• Ron Gabriel N. Añonuevo – BSIT Student


Project Purpose and Educational Value

The Student Grade Evaluator App was developed to strengthen understanding of programming fundamentals, object-oriented programming concepts, and practical system design.

The project provided hands-on experience in creating a complete system that accepts inputs, processes data, validates results, and generates structured outputs.

It also improved skills in debugging, modular programming, software testing, and academic system development.


Development Notes

• System design prioritizes simplicity and usability
• Validation ensures input reliability
• Modular design is implemented inside a single file
• The project emphasizes practical programming applications
• The system remains expandable for future improvements


Artificial Intelligence (AI) Usage Documentation

AI Tool Used
• ChatGPT by OpenAI
Role of AI in Development
1. System Design Guidance
AI was used to help outline the overall structure of the application, including how different components interact. It assisted in planning the system flow to ensure the project design is logical and efficient.
2. Code Optimization Support
The AI provided suggestions to improve code quality by making it cleaner, more efficient, and easier to maintain. It also helped identify better ways to write certain functions and reduce redundancy.
3. Debugging Assistance
AI was used to help analyze errors and unexpected behavior in the code. It suggested possible causes of bugs and provided fixes or improvements to resolve issues faster during development.
4. Feature Planning and Improvement
The AI assisted in brainstorming and refining project features. It helped suggest enhancements that improve usability, functionality, and overall user experience of the application.


Human Responsibility and Ethical Use

Although AI tools were used as support resources, all coding implementation, debugging, testing, design decisions, and validation were completed by the developer.

Final Note
The Student Grade Evaluator App represents the practical application of programming concepts, object-oriented principles, and software testing techniques.
