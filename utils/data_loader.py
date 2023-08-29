import json
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


def load_config(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"Configuration file {filename} not found.")
        raise
    except json.JSONDecodeError:
        logging.error(f"Error decoding the JSON configuration from {filename}.")
        raise


def load_question_pool(filename):
    try:
        with open(filename) as json_file:
            question_data = json.load(json_file)
            from models.question import Question  # local import to avoid cyclic dependencies
            return [Question(data) for data in question_data["questions"]]
    except FileNotFoundError:
        logging.error(f"Question pool file {filename} not found.")
        raise
    except json.JSONDecodeError:
        logging.error(f"Error decoding the JSON question data from {filename}.")
        raise
