from interfaces import IOutputWriter
from processor import GradeProcessor


class ConsoleOutputWriter(IOutputWriter):

    def write(self, student):
        processor = GradeProcessor()

        print("\n--- Academic Evaluation Result ---")
        print(f"Name: {student.name}")
        print(f"GWA: {student.gwa:.2f}")
        print(f"Target GWA: {student.goal_gwa}")
        print(f"Status: {student.status}")
        print(processor.compare_goal(student))

        print("\nSubjects:")
        for subject, grade in student.subjects.items():
            print(f"- {subject}: {grade}")