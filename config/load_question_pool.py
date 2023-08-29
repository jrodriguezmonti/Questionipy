from .models import Question

def load_question_pool(filename):
    try:
        with open(filename) as json_file:
            question_data = json.load(json_file)
            return [Question(data) for data in question_data["questions"]]
    except FileNotFoundError:
        logging.error(f"Question pool file {filename} not found.")
        raise
    except json.JSONDecodeError:
        logging.error(f"Error decoding the JSON question data from {filename}.")
        raise