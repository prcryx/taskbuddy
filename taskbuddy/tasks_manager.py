import typing as t

from taskbuddy import utils
from taskbuddy.database import DatabaseConnectionFactory, SQLiteAdapter
from taskbuddy.types import Task


class _DBConstants:
    TASKS_TABLE = "tasks"
    TASKS_COLUMN_ID = "id"
    TASKS_COLUMN_TASK = "task"
    TASKS_COLUMN_CREATED_AT = "createdAt"
    TASKS_COLUMN_DUE_DATE = "dueDate"
    TASKS_COLUMN_COMPLETED = "completed"


# Singleton instance
DB_CONSTANTS = _DBConstants()


# Task Related Functionalities
class TaskManager:
    def __init__(self, db_adapter: SQLiteAdapter):
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

        self.db_adapter.commit()
        self.db_adapter.close()

    # view all tasks [pending and completed]
    def view_all_tasks(self) -> t.List[Task]:
        query = f"""
            SELECT
                {DB_CONSTANTS.TASKS_COLUMN_ID},
                {DB_CONSTANTS.TASKS_COLUMN_TASK},
                {DB_CONSTANTS.TASKS_COLUMN_CREATED_AT},
                {DB_CONSTANTS.TASKS_COLUMN_DUE_DATE},
                {DB_CONSTANTS.TASKS_COLUMN_COMPLETED}
            FROM {DB_CONSTANTS.TASKS_TABLE};
            """
        self.db_adapter.execute(query)
        result_set = self.db_adapter.fetch_all()
        return [self._map_to_task(row) for row in result_set]
        # return []

    def _map_to_task(self, row: tuple) -> Task:
        """
        Map a database row to a Task type.
        """
        return Task.from_dict(
            {
                "id": row[0],
                "task": row[1],
                "created_at": utils.to_datestr(row[2]),
                "due": utils.to_datestr(row[3]),
                "status": row[4],
            }
        )


# Factory for creating a TaskManager instance
def create_task_manager(db_type="sqlite"):
    connection = DatabaseConnectionFactory.create_connection(db_type)
    db_adapter = SQLiteAdapter(connection)
    return TaskManager(db_adapter)
