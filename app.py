import tkinter as tk
from tkinter import messagebox

from processor import GradeProcessor
from student import Student


class GradeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Grade Evaluator App")
        self.root.geometry("400x500")

        self.processor = GradeProcessor()

        # Title
        tk.Label(root, text="Grade Evaluator", font=("Arial", 16)).pack(pady=10)

        # Name
        tk.Label(root, text="Name").pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        # Subjects
        self.subjects = []

        self.subject_frame = tk.Frame(root)
        self.subject_frame.pack(pady=10)

        # Header row
        header_frame = tk.Frame(self.subject_frame)
        header_frame.pack()

        tk.Label(header_frame, text="Subject", width=15, anchor="center").pack(side="left")
        tk.Label(header_frame, text="Grade", width=10, anchor="center").pack(side="left", padx=5)

        # First input row
        self.add_subject_fields()

        tk.Button(root, text="Add Subject", command=self.add_subject_fields).pack()

        # Goal
        tk.Label(root, text="Target GWA").pack()
        self.goal_entry = tk.Entry(root)
        self.goal_entry.pack()

        # Button
        tk.Button(root, text="Compute", command=self.compute).pack(pady=10)

        # Output
        self.result_label = tk.Label(root, text="", justify="left")
        self.result_label.pack(pady=10)

    def add_subject_fields(self):
        frame = tk.Frame(self.subject_frame)
        frame.pack()

        subject_entry = tk.Entry(frame, width=15)
        subject_entry.pack(side="left")

        grade_entry = tk.Entry(frame, width=10)
        grade_entry.pack(side="left", padx=5)

        self.subjects.append((subject_entry, grade_entry))

    def compute(self):
        try:
            name = self.name_entry.get()
            goal = float(self.goal_entry.get())

            subjects = {}
            for subject_entry, grade_entry in self.subjects:
                subject = subject_entry.get()
                grade = float(grade_entry.get())
                subjects[subject] = grade

            student = Student(name, subjects)
            student.set_goal(goal)

            student = self.processor.process(student)
            result = self.processor.compare_goal(student)

            output = f"Name: {student.name}\n"
            output += f"GWA: {student.gwa:.2f}\n"
            output += f"Target GWA: {student.goal_gwa}\n"
            output += f"Status: {student.status}\n"
            output += result + "\n\nSubjects:\n"

            for subject, grade in student.subjects.items():
                output += f"- {subject}: {grade}\n"

            self.result_label.config(text=output)

        except Exception as e:
            messagebox.showerror("Error", "Invalid input. Please check your values.")


if __name__ == "__main__":
    root = tk.Tk()
    app = GradeApp(root)
    root.mainloop()