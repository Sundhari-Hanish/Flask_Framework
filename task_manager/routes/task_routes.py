from flask import Blueprint, request, jsonify
from models.db import get_db_connection
from utils.response import success_response, error_response
task_bp = Blueprint('task_bp', __name__)

# CREATE TASK
@task_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """INSERT INTO tasks (title, description, status, priority, due_date) VALUES (%s, %s, %s, %s, %s)"""
    values = (
        data.get('title'),
        data.get('description'),
        data.get('status'),
        data.get('priority'),
        data.get('due_date')
    )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(success_response(message="Task created successfully"))

# GET ALL TASKS
@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(success_response(tasks))

# GET TASK BY ID
@task_bp.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tasks WHERE id = %s", (id,))
    task = cursor.fetchone()
    cursor.close()
    conn.close()
    if task:
        return jsonify(success_response(task))
    return jsonify(error_response("Task not found"))

# UPDATE TASK
@task_bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        UPDATE tasks
        SET title=%s, description=%s, status=%s, priority=%s, due_date=%s
        WHERE id=%s
    """
    values = (
        data.get('title'),
        data.get('description'),
        data.get('status'),
        data.get('priority'),
        data.get('due_date'),
        id
    )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(success_response(message="Task updated successfully"))

# DELETE TASK
@task_bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify(success_response(message="Task deleted successfully"))
