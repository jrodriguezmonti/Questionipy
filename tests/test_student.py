from models.student import Student


def test_student_creation():
    student = Student(1)
    assert student.id == 1
    assert student.number == "ST002"
    assert student.email == "student2@example.com"

    student_custom = Student(2, name="John", number="ST005", email="john@example.com")
    assert student_custom.name == "John"
    assert student_custom.number == "ST005"
    assert student_custom.email == "john@example.com"


def test_student_to_dict():
    student = Student(1)
    student_dict = student.to_dict()
    assert isinstance(student_dict, dict)
    assert student_dict == {'id': 1, 'name': 'Student 2', 'number': 'ST002', 'email': 'student2@example.com'}


def test_student_with_no_parameters():
    student = Student(3)
    assert student.number == "ST004"
    assert student.email == "student4@example.com"


def test_student_custom_parameters():
    student = Student(4, name="Alice", number="ST006", email="alice@example.com")
    assert student.name == "Alice"
    assert student.number == "ST006"
    assert student.email == "alice@example.com"


def test_student_creation_with_same_id():
    student1 = Student(1, name="Alice")
    student2 = Student(1, name="Bob")
    assert student1.name == "Alice"
    assert student2.name == "Bob"
    assert student1.number == student2.number
    assert student1.email != student2.email


def test_student_creation_without_email():
    student = Student(5, name="Eve", number="ST007")
    assert student.email == "student5@example.com"


def test_student_creation_with_same_name():
    student1 = Student(6, name="Charlie")
    student2 = Student(7, name="Charlie")
    assert student1.name == "Charlie"
    assert student2.name == "Charlie"
    assert student1.number != student2.number


def test_student_creation_with_default_values():
    student = Student(8)
    assert student.name == "Student 9"
    assert student.number == "ST009"
    assert student.email == "student9@example.com"


def test_student_creation_with_long_name():
    long_name = "X" * 100
    student = Student(9, name=long_name)
    assert student.name == long_name[:30]  # Should be truncated to 30 characters
