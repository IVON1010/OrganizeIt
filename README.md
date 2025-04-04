# OrganizeIt
OrganizeIt is a simple, efficient task management application built with Django. It helps users stay organized by providing an intuitive interface for managing their tasks, setting deadlines, and tracking progress. Whether you're handling personal to-dos or work-related projects, OrganizeIt offers a clean and user-friendly experience to stay on top of your tasks.

## Features
- **User Authentication**: Secure sign-up, login, and logout functionality, ensuring that each user has access to their personalized task list.

- **Task Management**: Easily add, edit, and delete tasks. Assign due dates and mark tasks as completed.

- **Task Prioritization**: Organize tasks by priority to ensure that important tasks are completed first.

- **Task Filtering**: Filter tasks by their status (completed or pending) to streamline the workflow.

- **Responsive Design**: Fully responsive web design built using Bootstrap, ensuring a seamless experience on both mobile and desktop devices.

## Technologies Used
- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.

- **SQLite**: A simple database solution for storing user data, task lists, and statuses.

- **HTML/CSS**: For structuring and styling the application.

- **Bootstrap**: For responsive front-end design to make the application accessible on all devices.

- **Django ORM**: To interact with the database through Python code, ensuring easy management of data.

- **Django Authentication**: For secure user authentication, including login, registration, and password management.

## Installation
### Prerequisites
Before you begin, ensure that you have the following installed on your machine:

- Python 3.8+

- pip (Python package manager)

## Steps to Run the Project Locally
Clone the Repository

```bash
git clone https://github.com/IVON1010/OrganizeIt.git
cd OrganizeIt
```
## Create a Virtual Environment

```bash
python -m venv venv
```
## Activate the Virtual Environment

On Windows:

```bash
venv\Scripts\activate
```
On macOS/Linux:

```bash
source venv/bin/activate
```
## Install Dependencies

```bash
pip install -r requirements.txt
```
## Apply Migrations

```bash
python manage.py migrate
```
### Create a Superuser (Optional)

To access the Django admin panel and manage the application, create a superuser:

```bash
python manage.py createsuperuser
```
Follow the prompts to create the superuser account.

## Run the Development Server

```bash
python manage.py runserver
```
## Visit the Application

Open your browser and navigate to http://127.0.0.1:8000/ to view the application.

## Usage
- **Sign Up / Log In**: To start using OrganizeIt, sign up for an account or log in if you already have one.

- **Manage Tasks**: Add new tasks with due dates, edit existing ones, or mark them as completed.

- **Prioritize Tasks**: Assign priority levels to your tasks and filter them to focus on what's important.

- **Responsive Design**: Whether on desktop or mobile, the application adjusts to provide the best user experience.

## Contributing
We welcome contributions to OrganizeIt! To contribute:

- Fork the repository.

- Create a new branch (git checkout -b feature-xyz).

- Make your changes.

- Commit your changes (git commit -am 'Add new feature').

- Push to the branch (git push origin feature-xyz).

- Open a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
