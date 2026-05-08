from student import Student


class GradeProcessor:

    def process(self, student: Student) -> Student:
        gwa = self._calculate_gwa(student.subjects)
        status = "Passed" if gwa >= 75 else "Failed"

        student.update_results(gwa, status)
        return student

    def _calculate_gwa(self, subjects: dict) -> float:
        return sum(subjects.values()) / len(subjects)

    def compare_goal(self, student: Student) -> str:
        if student.gwa >= student.goal_gwa:
            return "You reached your target GWA"
        return "You did not reach your target GWA"