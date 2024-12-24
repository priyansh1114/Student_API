# Student API

This is a Django-based API for managing student records, including CRUD (Create, Read, Update, Delete) operations. The project uses Poetry for dependency management.

## Features

- Create, read, update, and delete student records.
- Efficiently manage dependencies with Poetry.
- Simple and clean code structure.

## Requirements

- Python 3.8+
- Django 3.2+
- Poetry 1.1+

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/student-api.git
    cd student-api
    ```

2. **Install Poetry:**

    Follow the instructions on the Poetry website to install Poetry.

3. **Install dependencies:**

    ```bash
    poetry install
    ```

4. **Apply migrations:**

    ```bash
    poetry run python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    poetry run python manage.py runserver
    ```

## Usage

### API Endpoints

- **List all students:**

    ```http
    GET /students/
    ```

- **Retrieve a single student:**

    ```http
    GET /students/{id}/
    ```

- **Create a new student:**

    ```http
    POST /students/
    ```

- **Update a student:**

    ```http
    PUT /students/{id}/
    ```

- **Delete a student:**

    ```http
    DELETE /students/{id}/
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

