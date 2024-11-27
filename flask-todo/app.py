from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'  # Użyj SQLite jako bazy danych
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname' # Użyj PostgreSQL jako bazy danych
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)

# Tworzenie tabel w kontekście aplikacji
with app.app_context():
    db.create_all()  # Utwórz tabele w bazie danych

# Endpoint do odczytywania wszystkich zadań
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{'id': task.id, 'title': task.title, 'done': task.done} for task in tasks]), 200

# Endpoint do dodawania nowego zadania
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    task = Task(title=data['title'], done=data.get('done', False))
    db.session.add(task)
    db.session.commit()
    return jsonify({'id': task.id, 'title': task.title, 'done': task.done}), 201

# Endpoint do aktualizowania zadania
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    data = request.get_json()
    task.title = data.get('title', task.title)
    task.done = data.get('done', task.done)
    db.session.commit()
    return jsonify({'id': task.id, 'title': task.title, 'done': task.done}), 200

# Endpoint do usuwania zadania
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
