# Assignment Tracker

A Django-based web application for managing assignments, allowing teachers to create assignments by subject/category, students to submit answers, and teachers to view and grade results. The system supports user authentication and roles, provides assignment tracking, and offers result export features.

---

## Features

- User Authentication (Login & Logout)
- Teachers can create assignments with multiple questions.
- Students can submit answers for assignments.
- Teachers can view submitted answers, mark assignments, and provide feedback.
- View and manage assignment results.
- Export results as PDF or share via email.
- Responsive UI with Bootstrap 5 and Bootstrap Icons.
- Breadcrumb navigation and intuitive interface.

---

## Technologies Used

- Python 3.13
- Django 5.2
- Bootstrap 5
- SQLite (default, can be changed)
- html2pdf.js (for PDF export)
- Git and GitHub for version control

---

## Getting Started

### Prerequisites

- Python 3.13+
- pip
- Virtualenv (recommended)

### Installation

1. Clone the repo:
    ```bash
    git clone https://github.com/metroliv/assignment_tracker.git
    cd assignment_tracker
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser (optional but recommended):
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Open your browser and visit `http://127.0.0.1:8000/`

---

## Usage

- Register or login as a teacher or student.
- Teachers can create assignments and add questions.
- Students can answer assignments assigned to them.
- Teachers can view results, grade submissions, and provide feedback.
- Export results as PDF or share via email from the results page.

---

## Project Structure

- `assignments/` — main Django app handling assignments and results.
- `templates/` — HTML templates with Bootstrap styling.
- `static/` — static files (CSS, JS, images).
- `assignment_tracker/` — project settings and URLs.

---

## Contributing

Contributions are welcome! Please:

1. Fork the repo.
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to your branch: `git push origin feature/your-feature`
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions or feedback, please open an issue or contact me at:

- GitHub: [metroliv](https://github.com/metroliv)
- Email: victormulinge92@gmail.com.com

---

## Acknowledgments

- Thanks to Django and Bootstrap communities for their great tools.
- Inspired by many online tutorials and open source projects.
