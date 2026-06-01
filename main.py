class Student:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects
        self.goal = None  # ADD THIS

    def set_goal(self, goal):
        self.goal = goal

    def compute_average(self):
        return sum(self.subjects.values()) / len(self.subjects)

    def check_goal(self):
        if self.goal is None:
            return False
        return self.compute_average() >= self.goal


class GradeProcessor:

    def calculate_gwa(self, subjects):
        total = sum(subjects.values())
        gwa = total / len(subjects)
        return gwa

    def evaluate_performance(self, subjects):

        evaluation = {}

        for subject, grade in subjects.items():

            if grade >= 75:
                evaluation[subject] = "PASS"

            else:
                evaluation[subject] = "FAIL"

        return evaluation

    def compare_goal(self, student):

        if student.gwa >= student.goal_gwa:
            return "Goal Achieved"

        return "Goal Not Achieved"

    def process(self, student):

        gwa = self.calculate_gwa(student.subjects)

        evaluations = self.evaluate_performance(
            student.subjects
        )

        if gwa >= 75:
            status = "PASS"

        else:
            status = "FAIL"

        student.update_results(
            gwa,
            status,
            evaluations
        )

        return student


def main():

    print("\n===== STUDENT GRADE EVALUATOR APP =====\n")

    try:

        name = input(
            "Enter Student Name: "
        )

        num_subjects = int(
            input(
                "Enter Number of Subjects: "
            )
        )

        subjects = {}

        for i in range(num_subjects):

            print(
                f"\nSubject {i+1}"
            )

            subject = input(
                "Subject Name: "
            )

            grade = float(
                input(
                    "Grade: "
                )
            )

            while grade < 0 or grade > 100:

                print(
                    "Grade must be between 0 and 100."
                )

                grade = float(
                    input(
                        "Enter Grade Again: "
                    )
                )

            subjects[subject] = grade

        goal = float(
            input(
                "\nEnter Target GWA: "
            )
        )

        student = Student(
            name,
            subjects
        )

        student.set_goal(
            goal
        )

        processor = GradeProcessor()

        student = processor.process(
            student
        )

        goal_result = processor.compare_goal(
            student
        )

        print(
            "\n===== ACADEMIC EVALUATION RESULT ====="
        )

        print(
            f"Student Name: {student.name}"
        )

        print(
            f"GWA: {student.gwa:.2f}"
        )

        print(
            f"Target GWA: {student.goal_gwa}"
        )

        print(
            f"Overall Status: {student.status}"
        )

        print(
            f"Goal Comparison: {goal_result}"
        )

        print(
            "\nSubject Evaluation:"
        )

        for subject, result in student.evaluation.items():

            print(
                f"{subject}: {result}"
            )

    except ValueError:

        print(
            "\nInvalid Input. Please enter valid numbers."
        )


if __name__ == "__main__":
    main()