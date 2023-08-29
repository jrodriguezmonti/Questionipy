# Questionipy
An exam-assignment generator designed with Python and data feed with JSON. It is able to generate random questions, take a set of already defined questions and generate all the needed examen for a course. To make easier designing different examen for lots of people, and then revising them.
Questionipy is a Python application that allows you to create customized exams from a pool of questions and generate PDF files of the exams for students to take.

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

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to reach out if you have any questions or need further assistance!

**Author:** Juan Rodríguez Monti
**Email:** rmontijuan@gmail.com
