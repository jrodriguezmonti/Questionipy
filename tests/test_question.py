import pytest
from models.question import Question


def test_question_creation_multiple_choice():
    data = {
        "question": "What is the capital of France?",
        "type": "multiple_choice",
        "options": ["Paris", "Berlin", "Madrid", "Rome"]
    }
    question = Question(data)
    assert question.question == "What is the capital of France?"
    assert question.type == "multiple_choice"
    assert question.options == ["Paris", "Berlin", "Madrid", "Rome"]


def test_question_creation_true_false():
    data = {
        "question": "Is the Earth round?",
        "type": "true_false"
    }
    question = Question(data)
    assert question.question == "Is the Earth round?"
    assert question.type == "true_false"
    assert question.options == []


def test_question_creation_with_no_options():
    data = {
        "question": "Open-ended question",
        "type": "text"
    }
    question = Question(data)
    assert question.question == "Open-ended question"
    assert question.type == "text"
    assert question.options == []


def test_question_creation_multi_select():
    data = {
        "question": "Select the programming languages:",
        "type": "multi_select",
        "options": ["Python", "Java", "C++", "HTML"]
    }
    question = Question(data)
    assert question.question == "Select the programming languages:"
    assert question.type == "multi_select"
    assert question.options == ["Python", "Java", "C++", "HTML"]


def test_question_creation_code():
    data = {
        "question": "Write a Python function to calculate the factorial of a number.",
        "type": "code",
        "options": ["Code here"]
    }
    question = Question(data)
    assert question.question == "Write a Python function to calculate the factorial of a number."
    assert question.type == "code"
    assert question.options == ["Code here"]


def test_question_creation_code_evaluation():
    data = {
        "question": "Evaluate the following Python code:",
        "type": "code_evaluation",
        "options": ["Code here"]
    }
    question = Question(data)
    assert question.question == "Evaluate the following Python code:"
    assert question.type == "code_evaluation"
    assert question.options == ["Code here"]


def test_question_estimate_space_multiple_choice():
    data = {
        "question": "Choose the correct option.",
        "type": "multiple_choice",
        "options": ["Option A", "Option B", "Option C"]
    }
    question = Question(data)
    estimated_space = question.estimate_space()
    assert estimated_space == len("Choose the correct option.") + len("Option A") + len("Option B") + len(
        "Option C") + 3 * 15


def test_question_estimate_space_true_false():
    data = {
        "question": "Is this statement true or false?",
        "type": "true_false"
    }
    question = Question(data)
    estimated_space = question.estimate_space()
    assert estimated_space == len("Is this statement true or false?") + 2 * 15


def test_question_estimate_space_code():
    data = {
        "question": "Write a short Python program.",
        "type": "code",
        "options": ["Code here"]
    }
    question = Question(data)
    estimated_space = question.estimate_space()
    assert estimated_space == len("Write a short Python program.") + len("Code here") + 15


def test_question_estimate_space_code_evaluation():
    data = {
        "question": "Evaluate the given code.",
        "type": "code_evaluation",
        "options": ["Code here"]
    }
    question = Question(data)
    estimated_space = question.estimate_space()
    assert estimated_space == len("Evaluate the given code.") + len("Code here") + 15


def test_question_incorrect_type():
    data = {
        "question": "What is the capital of France?",
        "type": "invalid_type",
        "options": ["Paris", "Berlin", "Madrid", "Rome"]
    }
    with pytest.raises(ValueError) as e:
        Question(data)
    assert str(e.value) == "Invalid question type: invalid_type"


def test_question_incorrect_option_format():
    data = {
        "question": "Choose an option.",
        "type": "multiple_choice",
        "options": "Option A"
    }
    with pytest.raises(ValueError) as e:
        Question(data)
    assert str(e.value) == "Options should be a list."


def test_question_missing_code_for_evaluation():
    data = {
        "question": "Write a Python program to calculate the factorial of a number.",
        "type": "code_evaluation",
        "options": ["Code here"]
    }
    with pytest.raises(ValueError) as e:
        Question(data)
    assert str(e.value) == "Code for evaluation is missing for the question."
