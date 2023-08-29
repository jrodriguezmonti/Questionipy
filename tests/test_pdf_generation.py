import os
import pytest
from models.question import Question
from pdf_generator.pdf_generator import generate_pdf


def test_generate_pdf():
    question = Question({"question": "What is 2 + 2?", "type": "multiple_choice", "options": ["3", "4"]})
    student_info = {"id": 1}
    pdf_filename = "test_exam.pdf"
    generate_pdf([question], student_info, pdf_filename)
    assert os.path.exists(pdf_filename)
    os.remove(pdf_filename)


def test_generate_pdf_with_long_student_name():
    question = Question({"question": "What is 2 + 2?", "type": "multiple_choice", "options": ["3", "4"]})
    student_info = {"id": 1, "name": "John Doe John Doe John Doe"}  # Long name
    pdf_filename = "long_name_exam.pdf"
    generate_pdf([question], student_info, pdf_filename)
    assert os.path.exists(pdf_filename)
    os.remove(pdf_filename)


def test_generate_pdf_with_empty_questions():
    student_info = {"id": 1}
    pdf_filename = "empty_exam.pdf"
    generate_pdf([], student_info, pdf_filename)
    assert os.path.exists(pdf_filename)
    os.remove(pdf_filename)


def test_generate_pdf_with_multiple_pages():
    question_pool = [
        Question({"question": f"Q{i}", "type": "multiple_choice", "options": ["A", "B"]}) for i in range(20)
    ]
    student_info = {"id": 1}
    pdf_filename = "multiple_page_exam.pdf"
    generate_pdf(question_pool, student_info, pdf_filename)
    assert os.path.exists(pdf_filename)
    os.remove(pdf_filename)


def test_generate_pdf_with_invalid_student_id():
    question = Question({"question": "What is 2 + 2?", "type": "multiple_choice", "options": ["3", "4"]})
    student_info = {"id": "invalid_id"}  # Invalid ID
    pdf_filename = "invalid_id_exam.pdf"
    with pytest.raises(TypeError) as e:
        generate_pdf([question], student_info, pdf_filename)
    assert "id must be int" in str(e.value)


def test_generate_pdf_with_missing_student_id():
    question = Question({"question": "What is 2 + 2?", "type": "multiple_choice", "options": ["3", "4"]})
    student_info = {}  # Missing ID
    pdf_filename = "missing_id_exam.pdf"
    with pytest.raises(KeyError) as e:
        generate_pdf([question], student_info, pdf_filename)
    assert "'id'" in str(e.value)


def test_generate_pdf_with_invalid_filename():
    question = Question({"question": "What is 2 + 2?", "type": "multiple_choice", "options": ["3", "4"]})
    student_info = {"id": 1}
    pdf_filename = "/invalid/test_exam.pdf"  # Invalid path
    with pytest.raises(FileNotFoundError) as e:
        generate_pdf([question], student_info, pdf_filename)
    assert "No such file or directory" in str(e.value)


def test_generate_pdf_with_no_questions():
    student_info = {"id": 1}
    pdf_filename = "no_questions_exam.pdf"
    generate_pdf([], student_info, pdf_filename)
    assert os.path.exists(pdf_filename)
    os.remove(pdf_filename)
