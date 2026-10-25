# Daily Task Manager

## Overview

**Daily Task Manager** is a Django web application designed to help users organize their daily activities, manage tasks, and track their progress. The application provides a structured way to create, categorize, and manage tasks through a simple and intuitive interface.

The project demonstrates the use of Django models, forms, class-based views, template rendering, and database relationships.

## Features

- **User Profiles** – Create and manage user profiles with a unique username and email address.
- **Task Management** – Create, view, edit, and manage daily tasks.
- **Task Status Tracking** – Organize tasks by status:
  - `TODO`
  - `IN_PROGRESS`
  - `DONE`
- **Categories** – Organize tasks into categories, such as Education, Hobby, Work, and Personal.
- **Task Descriptions** – Add optional descriptions with additional information.
- **Due Dates** – Set optional deadlines for tasks.
- **Automatic Timestamps** – Record when a task is created.
- **Data Validation** – Validate user input according to the defined model requirements.

## Technologies

- Python
- Django
- PostgreSQL
- HTML
- CSS
- Git
- GitHub

## Project Structure

The application is organized into separate Django apps to maintain a clear separation of responsibilities.

```text
DailyTaskManager/
├── profiles/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── tasks/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── categories/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── templates/
├── static/
├── manage.py
└── requirements.txt
```

*Note: The structure above is illustrative and should be adjusted to match the actual project files.*

## Data Models

### Profile

Represents a user profile within the application.

- `username` – Required, 2–15 characters; letters, numbers, and underscores only.
- `email` – Required email address.
- `age` – Optional integer greater than or equal to zero.

### Task

Represents an individual task.

- `title` – Required text, maximum 100 characters.
- `description` – Optional text.
- `status` – Task status: TODO, IN_PROGRESS, or DONE.
- `created_at` – Automatically generated creation timestamp.
- `due_date` – Optional deadline.
- `profile` – Required relationship to a profile.
- `category` – Optional relationship to a category.

### Category

Represents a category used to group related tasks.

Categories can be used to distinguish different areas of daily life, such as education, hobbies, work, and personal activities.

## Installation and Setup

### Prerequisites

- Python 3.10 or later, compatible with the installed Django version.
- PostgreSQL.
- Git.

### 1. Clone the repository

```bash
git clone <repository-url>
cd DailyTaskManager
```

Replace `<repository-url>` with the actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` does not exist yet, create it after installing the project's dependencies.

### 4. Configure the database

Configure PostgreSQL connection settings using environment variables or the project's local configuration.

Do not commit database passwords, secret keys, or other sensitive configuration values to GitHub.

### 5. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open the local development address:

http://127.0.0.1:8000/

## Validation Rules

The application applies validation rules to maintain data consistency:

- Profile usernames must contain only letters, numbers, and underscores.
- Usernames must be between 2 and 15 characters long.
- Email addresses are required and must have a valid format.
- Age is optional and cannot be negative.
- Task titles are required and limited to 100 characters.
- Task descriptions and due dates are optional.

## Future Improvements

Potential extensions include:

- Task search and filtering.
- Filtering tasks by status, category, and due date.
- Sorting tasks by creation date or deadline.
- Dashboard with task statistics.
- Overdue task indicators.
- Improved responsive design.
- Automated tests for models, forms, and views.
- User authentication and permissions, if not already implemented.
- Deployment to a cloud hosting platform.

## Learning Objectives

This project provides practical experience with:

- Django project and application structure.
- Model relationships and database design.
- Django forms and data validation.
- Class-based views and URL routing.
- HTML templates and CSS styling.
- PostgreSQL integration.
- Git version control and GitHub collaboration.

## License

The licensing terms have not yet been specified. Add a license if you intend to distribute or publish the project under particular reuse conditions.
