from app import db
import uuid


class Task(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    task = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    priority = db.Column(db.String(50))
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Task {self.task}>"
