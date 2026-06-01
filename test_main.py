import pytest
from main import Student, GradeProcessor

# ---------- FIXTURES ----------

@pytest.fixture
def sample_student():
    subjects = {
        "Math": 85,
        "Science": 90,
        "English": 80
    }
    student = Student("John", subjects)
    student.set_goal(85)
    return student


@pytest.fixture
def processor():
    return GradeProcessor()


# ---------- STUDENT TESTS ----------

def test_student_initialization(sample_student):
    assert sample_student.name == "John"
    assert sample_student.subjects["Math"] == 85
    assert sample_student.goal == 85


def test_average_computation(sample_student):
    avg = sample_student.compute_average()
    assert avg == pytest.approx(85.0)


def test_goal_check(sample_student):
    result = sample_student.check_goal()
    assert isinstance(result, bool)


# ---------- PROCESSOR TESTS ----------

def test_processor_exists(processor):
    assert processor is not None