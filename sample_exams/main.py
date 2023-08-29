import asyncio
import logging
from utils.data_loader import load_config, load_question_pool
from models.student import Student
from models.question import calculate_max_questions_per_page, generate_exam
from pdf_generator.pdf_generator import generate_pdf

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


# We are going to use async functions to make it more robust, faster and scalable
async def main():
    config = load_config("config/config.json")
    question_pool = load_question_pool("config/larger_question_pool.json")

    # This function is going to calculate the number of max questions per page
    max_questions_per_page = calculate_max_questions_per_page(config['max_chars_per_page'], question_pool)
    estimated_chars_per_question = sum(q.estimate_space() for q in question_pool) / len(question_pool)

    logging.info(f"Max Questions per Page: {max_questions_per_page}")

    max_questions = int(config['max_chars_per_page'] / estimated_chars_per_question)

    # We are going to evaluate here the desired questions per exam over the max possible questions
    if config['desired_questions_per_exam'] > max_questions:
        logging.warning(
            f"'desired_questions_per_exam' ({config['desired_questions_per_exam']}) exceeds the maximum allowable "
            f"questions ({max_questions}). Setting to the maximum value.")
        config['desired_questions_per_exam'] = max_questions

    for student_id in range(config['num_students']):
        student = Student(student_id, name=None)
        max_questions = int(config['max_chars_per_page'] / estimated_chars_per_question)
        exam = generate_exam(question_pool, min(config['desired_questions_per_exam'], max_questions))
        pdf_filename = f"exam_{student_id + 1}.pdf"
        logging.debug(f"Generating PDF for student: {student.name}, with questions: {[q.question for q in exam]}")
        generate_pdf(exam, student.to_dict(), pdf_filename, config['exam_title'], config['course_name'])

        logging.info(f"Generated exam for {student.name}")

    logging.info("All exams generated successfully.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")
