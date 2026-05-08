class Student:
    def __init__(self, name: str, subjects: dict):
        self._name = name
        self._subjects = subjects
        self._gwa = 0.0
        self._goal_gwa = 0.0
        self._status = ""

    @property
    def name(self):
        return self._name

    @property
    def subjects(self):
        return self._subjects.copy()

    @property
    def gwa(self):
        return self._gwa

    @property
    def goal_gwa(self):
        return self._goal_gwa

    @property
    def status(self):
        return self._status

    def set_goal(self, goal: float):
        self._goal_gwa = goal

    def update_results(self, gwa: float, status: str):
        self._gwa = gwa
        self._status = status