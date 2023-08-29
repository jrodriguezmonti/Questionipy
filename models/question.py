import random


class Question:
    def __init__(self, data):
        self.question = data['question']
        self.type = data['type']
        self.options = data.get('options', [])

    def estimate_space(self):
        question_length = len(self.question)
        if self.type in ('multiple_choice', 'multi_select'):
            question_length += len(self.options) * 15
        elif self.type in ('true_false', 'code', 'code_evaluation'):
            question_length += 50
        return question_length


def estimate_question_space(question):
    return question.estimate_space()


def calculate_max_questions_per_page(max_chars_per_page, questions):
    estimated_chars_per_question = sum(estimate_question_space(q) for q in questions) / len(questions)
    max_questions_per_page = max_chars_per_page // estimated_chars_per_question
    return max_questions_per_page


def generate_exam(questions, num_questions):
    random.shuffle(questions)
    return questions[:num_questions]
