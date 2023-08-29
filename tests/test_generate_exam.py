import pytest
from models.question import Question, generate_exam


def test_generate_exam():
    question_pool = [
        Question({"question": "Q1", "type": "multiple_choice", "options": ["A", "B"]}),
        Question({"question": "Q2", "type": "true_false"}),
        Question({"question": "Q3", "type": "code", "options": ["Code here"]}),
    ]
    exam = generate_exam(question_pool, 2)
    assert len(exam) == 2
    assert isinstance(exam[0], Question)
    assert isinstance(exam[1], Question)


def test_generate_exam_insufficient_questions():
    question_pool = [
        Question({"question": "Q1", "type": "multiple_choice", "options": ["A", "B"]}),
        Question({"question": "Q2", "type": "true_false"}),
    ]
    exam = generate_exam(question_pool, 5)  # More questions requested than available
    assert len(exam) == 2


def test_generate_exam_with_invalid_question_types():
    question_pool = [
        Question({"question": "Q1", "type": "invalid_type", "options": ["A", "B"]}),
        Question({"question": "Q2", "type": "true_false"}),
    ]
    with pytest.raises(ValueError) as e:
        generate_exam(question_pool, 2)
    assert str(e.value) == "Invalid question type: invalid_type"


def test_generate_exam_with_duplicate_questions():
    question_pool = [
        Question({"question": "Q1", "type": "multiple_choice", "options": ["A", "B"]}),
        Question({"question": "Q1", "type": "true_false"}),  # Duplicate question
    ]
    with pytest.raises(ValueError) as e:
        exam = generate_exam(question_pool, 2)
    assert str(e.value) == "Duplicated question in the question pool"


def test_generate_exam_with_zero_questions():
    question_pool = []
    exam = generate_exam(question_pool, 0)
    assert len(exam) == 0


def test_generate_exam_zero_desired_questions():
    question_pool = [
        Question({"question": "Q1", "type": "multiple_choice", "options": ["A", "B"]}),
        Question({"question": "Q2", "type": "true_false"}),
    ]
    exam = generate_exam(question_pool, 0)
    assert len(exam) == 0


def test_generate_exam_with_large_pool():
    question_pool = [
        Question({"question": f"Q{i}", "type": "multiple_choice", "options": ["A", "B"]}) for i in range(100)
    ]
    exam = generate_exam(question_pool, 10)
    assert len(exam) == 10


def test_generate_exam_with_exact_questions():
    question_pool = [
        Question({"question": f"Q{i}", "type": "multiple_choice", "options": ["A", "B"]}) for i in range(10)
    ]
    exam = generate_exam(question_pool, 10)
    assert len(exam) == 10


def test_generate_exam_with_empty_pool():
    question_pool = []
    exam = generate_exam(question_pool, 5)
    assert len(exam) == 0
