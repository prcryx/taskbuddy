from taskbuddy.database import DatabaseConnectionFactory, SQLiteAdapter
from taskbuddy.entities.task import Task


class TaskManager:
    def __init__(self, db_adapter):
        self.db_adapter = db_adapter

    def add_task(self, task: Task):
        query = """
        INSERT INTO tasks (task, createdAt, dueDate, completed)
        VALUES (?, ?, ?, ?)
        """
        self.db_adapter.execute(
            query,
            (
                task.get_task(),
                task.get_creation_date(),
                task.get_due_date(),
                task.get_status(),
            ),
        )


# Factory for creating a TaskManager instance
def create_task_manager(db_type="sqlite"):
    connection = DatabaseConnectionFactory.create_connection(db_type)
    db_adapter = SQLiteAdapter(connection)
    return TaskManager(db_adapter)
