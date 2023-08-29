# Questionipy
Questionipy is a Python application designed to facilitate exam and assignment generation. Powered by JSON data feeds, it can randomly generate questions or utilize pre-defined ones to create comprehensive exams for educational courses, academia and more. This tool streamlines the process of crafting varied exams for multiple individuals, simplifying both design and review. With Questionipy, you can effortlessly customize exams from a diverse question pool and effortlessly produce PDF files that students can use for assessments.

## Features

- Create exams by selecting a specified number of questions from a question pool.
- Supports various question types including multiple choice, true/false, and code-based questions.
- Customize the exam title, course name, and other details in the generated PDF.
- Automatically estimates the number of questions that can fit on each exam page.
- Generates clean and formatted PDF files ready for printing or distribution to students.
- Auto scaling the PDF with new lines when needed.
- Async creation of PDF for a more scalable and powerful creation of files.

## Prerequisites

- Python 3.6 or higher
- Pip package manager

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory:
```
cd questionipy
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```

## Configuration

1. Edit the `config/config.json` or `config/larger_question_pool.json` to use the included sample file to customize your exam settings, such as maximum characters per page, desired questions per exam, and number of students.
2. Place your question pool in the `config/question_pool.json` file. The question pool should be in the specified JSON format.

## Usage

1. Run the application by executing the main script:

```
python main.py
```
2. The application will generate PDF exam files for each student based on the configuration and question pool.

## Customization

- You can customize the appearance of the generated PDFs by modifying the formatting in the `generate_pdf_content` function.
- To add more question types or modify existing ones, you can update the `Question` class and the `format_question` function in `main.py`.

- ## Sample exams

- You can find under the folder `sample_exams` 10 automatically generated exams, using the sample pool of questions included with the following settings:

```json
{
  "max_chars_per_page": 2000,
  "desired_questions_per_exam": 10,
  "num_students": 20,
  "exam_title": "First Quarter Exam",
  "course_name": "Data Structures and Algorithms by Larry David"
}
```

- ## Pool of questions

- You can find the following JSON File with the pool of questions to feed Questionipy:

```json
{
    "questions": [
      {
        "type": "text",
        "question": "Explain the concept of object-oriented programming."
      },
      {
        "type": "multiple_choice",
        "question": "Which of the following is an example of a programming language?",
        "options": ["HTML", "CSS", "Python", "JSON", "XML"],
        "correct_answer": "Python"
      },
      {
        "type": "true_false",
        "question": "The Python programming language was named after a snake.",
        "correct_answer": true
      },
      {
        "type": "multi_select",
        "question": "Which of the following are Python frameworks for web development?",
        "options": ["Django", "Flask", "React", "Vue.js", "Angular"],
        "correct_answers": ["Django", "Flask"]
      },
      {
        "type": "multi_select",
        "question": "Which of the following are key benefits of pair programming?",
        "options": ["Reduced development time", "Increased code quality", "Limited communication", "Enhanced team collaboration", "Higher bug density"],
        "correct_answers": ["Reduced development time", "Increased code quality", "Enhanced team collaboration"]
      }
    ]
  }
```

## ToDo

This is a first alpha release with many work remaining. 

Some of the big stuff:
- CSV export support
- Database storage of data
- Automatic corrections
- More and with deeper details tests

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to reach out if you have any questions or need further assistance!

**Author:** Juan Rodríguez Monti
**Email:** rmontijuan@gmail.com
