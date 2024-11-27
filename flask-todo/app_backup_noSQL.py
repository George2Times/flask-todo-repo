from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []  # Lista zadań przechowywana w pamięci

# Endpoint do odczytywania wszystkich zadań
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

# Endpoint do dodawania nowego zadania
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'done': data.get('done', False)
    }
    tasks.append(task)
    return jsonify(task), 201

# Endpoint do aktualizowania zadania
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    data = request.get_json()
    task['title'] = data.get('title', task['title'])
    task['done'] = data.get('done', task['done'])
    return jsonify(task), 200

# Endpoint do usuwania zadania
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    tasks.remove(task)
    return jsonify({'message': 'Task deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
