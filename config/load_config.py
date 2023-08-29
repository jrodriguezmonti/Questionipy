import logging
import json

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