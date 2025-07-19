from app import db
from app.models import Todo

def get_all_todos():
    return Todo.query.all()

def add_todo(title):
    if not title or not title.strip():
        return False  # Validation
    todo = Todo(title=title.strip(), complete=False)
    db.session.add(todo)
    db.session.commit()
    return True

def toggle_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        todo.complete = not todo.complete
        db.session.commit()

def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
