
# Flask To-Do App

A REST API application built with Flask that allows users to create, read, update, and delete tasks.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)

## Installation

To get started, you need to clone this repository and install the necessary dependencies.

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/flask-todo.git
   cd flask-todo
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

After installation, you can run the application using:

```sh
python flask-todo/app.py
```

The server will start at `http://127.0.0.1:5000`. You can use any REST client like Postman, or tools like `curl`, to interact with the API.

The application uses Flask for the API and optionally SQLite for data persistence.

## API Endpoints

### GET /tasks
- Retrieves all tasks.
- Example:
  ```sh
  curl http://127.0.0.1:5000/tasks
  ```

### GET /tasks/<id>
- Retrieves a specific task by its ID.
- Example:
  ```sh
  curl http://127.0.0.1:5000/tasks/1
  ```

### POST /tasks
- Creates a new task.
- Example:
  ```sh
  curl -X POST -H "Content-Type: application/json" -d '{"title": "Learn Flask"}' http://127.0.0.1:5000/tasks
  ```

### PUT /tasks/<id>
- Updates an existing task.
- Example:
  ```sh
  curl -X PUT -H "Content-Type: application/json" -d '{"title": "Learn Flask and REST", "done": true}' http://127.0.0.1:5000/tasks/1
  ```

### DELETE /tasks/<id>
- Deletes a task.
- Example:
  ```sh
  curl -X DELETE http://127.0.0.1:5000/tasks/1
  ```

## Testing

You can also test the API using PowerShell:

- Fetch all tasks:
  ```sh
  Invoke-RestMethod -Uri http://127.0.0.1:5000/tasks -Method Get
  ```
- Add a new task:
  ```sh
  Invoke-RestMethod -Uri http://127.0.0.1:5000/tasks -Method Post -Body '{"title": "Learn Flask"}' -ContentType "application/json"
  ```
- Update a task:
  ```sh
  Invoke-RestMethod -Uri http://127.0.0.1:5000/tasks/1 -Method Put -Body '{"title": "Learn Flask and REST", "done": true}' -ContentType "application/json"
  ```
- Delete a task:
  ```sh
  Invoke-RestMethod -Uri http://127.0.0.1:5000/tasks/1 -Method Delete
  ```

## Requirements

The required Python packages are listed in the `requirements.txt` file:

- Flask
- Flask-SQLAlchemy

Install them with:

```sh
pip install -r requirements.txt
```

## Project Structure

```
flask-todo/
│
├── flask-todo/
│   ├── instance/
│   ├── utils/
│   ├── app.py
│   └── requirements.txt
│
├── venv/
│
└── README.md
```
