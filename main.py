class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, subjects):
        super().__init__(name)

        self.subjects = subjects
        self.goal = None

        self.gwa = 0
        self.status = ""
        self.evaluation = {}

    def set_goal(self, goal):
        self.goal = goal

    def compute_average(self):
        return sum(self.subjects.values()) / len(self.subjects)

    def check_goal(self):
        if self.goal is None:
            return False

        return self.gwa >= self.goal

    def update_results(
        self,
        gwa,
        status,
        evaluation
    ):

        self.gwa = gwa
        self.status = status
        self.evaluation = evaluation


class GradeProcessor:

    def calculate_gwa(
        self,
        subjects
    ):

        total = sum(
            subjects.values()
        )

        gwa = total / len(subjects)

        return gwa

    def evaluate_performance(
        self,
        subjects
    ):

        evaluation = {}

        for subject, grade in subjects.items():

            if grade >= 75:

                evaluation[subject] = "PASS"

            else:

                evaluation[subject] = "FAIL"

        return evaluation

    def compare_goal(
        self,
        student
    ):

        if student.gwa >= student.goal:

            return "Goal Achieved"

        return "Goal Not Achieved"

    def process(
        self,
        student
    ):

        gwa = self.calculate_gwa(
            student.subjects
        )

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



class AdvancedGradeProcessor(
    GradeProcessor
):

    def calculate_gwa(
        self,
        subjects
    ):

        
        return super().calculate_gwa(
            subjects
        )


def save_results(student):

    with open(
        "student_results.txt",
        "w"
    ) as file:

        file.write(
            f"Student: {student.name}\n"
        )

        file.write(
            f"GWA: {student.gwa:.2f}\n"
        )

        file.write(
            f"Goal: {student.goal}\n"
        )

        file.write(
            f"Status: {student.status}\n"
        )

        file.write(
            "Subject Evaluation:\n"
        )

        for subject, result in student.evaluation.items():

            file.write(
                f"{subject}: {student.subjects[subject]} - {result.lower()}\n"
            )


def main():

    print(
        "\n===== STUDENT GRADE EVALUATOR APP =====\n"
    )

    try:

        name = input(
            "Enter Student Name: "
        )

        num_subjects = int(
            input(
                "Enter Number of Subjects: "
            )
        )

        while num_subjects <= 0:

            print(
                "Subjects must be greater than 0."
            )

            num_subjects = int(
                input(
                    "Enter Number Again: "
                )
            )

        subjects = {}

        for i in range(num_subjects):

            print(
                f"\nSubject {i+1}"
            )

            subject = input(
                "Enter subject: "
            )

            grade = float(
                input(
                    "Enter grade: "
                )
            )

            while grade < 0 or grade > 100:

                print(
                    "Grade must be between 0 and 100."
                )

                grade = float(
                    input(
                        "Enter grade again: "
                    )
                )

            subjects[subject] = grade

        goal = float(
            input(
                "\nEnter your target GWA: "
            )
        )

        student = Student(
            name,
            subjects
        )

        student.set_goal(
            goal
        )

        processor = AdvancedGradeProcessor()

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
            f"Target GWA: {student.goal}"
        )

        print(
            f"Overall Status: {student.status}"
        )

        if goal_result == "Goal Achieved":
            print("Target GWA Achieved")
        else:
            print("You did not reach your target GWA")

        print(
            "\nSubject Evaluation:"
        )

        for subject, result in student.evaluation.items():

            print(
                f"- {subject}: {student.subjects[subject]} - {result.lower()}"
            )

        save_results(
            student
        )

        print(
            "\nResults saved to student_results.txt"
        )

    except ValueError:

        print(
            "\nInvalid Input. Please enter valid numbers."
        )


if __name__ == "__main__":

    main()
