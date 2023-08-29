import logging
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


def create_header_content(student_info, styles, exam_title, course_name):
    header_style = styles["Heading1"]
    header_content = [
        Paragraph(exam_title, header_style),
        Paragraph(course_name, header_style),
        Paragraph(f"Date: {datetime.now():%Y-%m-%d}", header_style),
        Paragraph(f"Identifier: {student_info['number']}", header_style),
        Spacer(1, 0.5 * inch)
    ]
    return header_content


def format_question(question, question_num, styles):
    formatted_question = f"{question_num}. {question.question}"

    # Handle different question types
    if question.type == 'multiple_choice':
        choices = "\n".join([f"   {chr(65 + i)}. {opt}" for i, opt in enumerate(question.options)])
        formatted_question += f"\n{choices}"

    elif question.type == 'multi_select':
        choices = "\n".join([f"   {chr(65 + i)}. [ ] {opt}" for i, opt in enumerate(question.options)])
        formatted_question += f"\n{choices}"

    elif question.type == 'true_false':
        formatted_question += "\n   [ ] True\n   [ ] False"

    elif question.type == 'code':
        # Check if options are present before accessing to avoid failing if there are no options
        if not question.options:
            logging.warning(f"Question '{question.question}' of type 'code' missing options.")
        else:
            formatted_question += f"\n{question.options[0]}"

    elif question.type == 'code_evaluation':
        if not question.options:
            logging.warning(f"Question '{question.question}' of type 'code_evaluation' missing options.")
        else:
            formatted_question += "\nEvaluate the following code and write the output:"
            formatted_question += f"\n{question.options[0]}"

    return Paragraph(formatted_question, styles["Normal"])


def generate_pdf_content(exam, student_info, styles, exam_title, course_name):
    content = []
    content.extend(create_header_content(student_info, styles, exam_title, course_name))

    for question_num, question in enumerate(exam, start=1):
        content.append(format_question(question, question_num, styles))
        content.append(Spacer(1, 12))

    return content


def generate_pdf(exam, student_info, pdf_filename, exam_title="Exam", course_name="Course"):
    try:
        logging.debug(f"Generating PDF for {student_info['name']}. Exam length: {len(exam)}")
        doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
        styles = getSampleStyleSheet()
        story = generate_pdf_content(exam, student_info, styles, exam_title, course_name)
        doc.build(story)
        logging.debug(f"Finished generating PDF for {student_info['name']}")
    except Exception as e:
        logging.error(f"Error generating PDF for {student_info['name']}. Error: {e}")
        raise
