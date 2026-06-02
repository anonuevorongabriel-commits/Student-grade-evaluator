Student Grade Evaluator App

Application Description

The Student Grade Evaluator App is a standalone Python application developed using a single-file structure to help students efficiently compute, monitor, and evaluate their academic performance. The system automates grade processing tasks that are often done manually, reducing calculation errors and improving the speed and accuracy of academic evaluation.
The application follows an Input → Process → Output model where users input grades, the system processes academic data, and structured evaluation results are generated automatically. The application was designed as a lightweight offline system that requires no internet connection or external database.
Core Features
The Student Grade Evaluator Application provides several core features that assist students in monitoring academic performance, computing grades, and evaluating progress toward academic goals. These features are designed to simplify grade computation and provide organized academic feedback.
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
The application applies Object-Oriented Programming (OOP) principles to organize code efficiently and improve maintainability. These concepts allow the program to separate responsibilities, improve readability, and support future expansion.

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
The development of the Student Grade Evaluator Application uses programming tools, frameworks, and concepts that support computation, testing, and software organization. These technologies work together to ensure functionality, maintainability, and reliability.
• Python – served as the primary programming language used to build the entire application. It was used to create the classes, functions, conditional statements, loops, and computations required for processing grades, calculating the General Weighted Average (GWA), and generating academic evaluation outputs.
• Pytest – used as the automated testing framework for verifying that different components of the application function correctly. It was applied to test grade computations, input validations, object initialization, and evaluation methods to ensure system reliability and reduce errors during development.
• Object-Oriented Programming Principles – Used to structure the project into organized classes and objects. The Student class was used for storing student-related information, while processing and evaluation logic were separated into dedicated methods and classes to improve maintainability and readability. 
• File Handling Operations – Implemented to support reading, writing, or storing academic information when necessary. This functionality allows the application to manage student records or generated outputs more efficiently within the program workflow.
• Core Programming Logic  – applied throughout the project using conditions, loops, calculations, and decision-making structures. These logical processes were essential for validating inputs, computing GWA values, comparing goals, and determining academic standing.
• Offline Execution Environment –The application was designed to operate entirely offline without requiring internet connectivity. This allows users to run the program locally on their devices while maintaining full access to grade evaluation features regardless of network availability.
System Workflow
The system workflow describes the sequence of operations performed by the application from data input to result generation. This process ensures that user inputs are validated, processed, and transformed into meaningful academic evaluations.
1.	User inputs student information and subject grades
2.	The system validates the entered data
3.	Grades are processed, and GWA is computed
4.	Goal GWA is compared with computed results
5.	Academic evaluation results are displayed
6.	User reviews generated evaluation output

PROJECT STRUCTURE
Grade Evaluator App
│
├── main.py
│ Contains all system logic including the Student class
│ Contains the GradeProcessor class
│ Handles grade evaluation and GWA computation
│ Includes goal setting and goal comparison features
│ Manages input validation and output display
│
├── test_main.py
│ Contains all pytest unit tests for the application
│ Tests student initialization and grade storage
│ Tests GWA computation and status evaluation
│ Tests goal setting and goal comparison
│ Tests invalid input handling and edge cases
│
└── README.md
    Provides a complete overview of the project
    Includes features, design rationale, and workflow
    Contains instructions on how to run the system and tests
    Documents technologies used and development notes
How to Run the System
1.	Requirements
• Python 3.x installed
2.	Clone repository
3.	Navigate to Project Folder
Student Grade Evaluator App
4.	Run the Application
Main.py

Running Tests
You can run unit tests using:
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
The AI assisted in brainstorming and refining project features. It helped suggest enhancements that improve usability, functionality, and overall user experience of the application. Human Responsibility and Ethical Use
Although AI tools were used as support resources, all coding implementation, debugging, testing, design decisions, and validation were completed by the developer.

Final Note
The Student Grade Evaluator App represents the practical application of programming concepts, object-oriented principles, and software testing techniques.

