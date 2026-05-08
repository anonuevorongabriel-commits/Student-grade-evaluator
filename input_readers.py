from interfaces import IInputReader
from student import Student


class ConsoleInputReader(IInputReader):

    def read(self) -> Student:
        name = input("Enter student name: ")

        subjects = {}
        count = int(input("Enter number of subjects: "))

        for _ in range(count):
            subject = input("Enter subject name: ")
            grade = float(input("Enter grade: "))
            subjects[subject] = grade

        goal = float(input("Enter your target GWA: "))

        student = Student(name, subjects)
        student.set_goal(goal)

        return student