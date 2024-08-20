from dataclasses import dataclass, field
from datetime import datetime
from taskbuddy.utils import parse_to_datetime, to_datestr
from taskbuddy.constants import DD_MM_YYYY_HH_MM


@dataclass
class Task:
    task: str
    due_date: datetime
    created_at: datetime = field(default_factory=datetime.now)
    status: bool = False
    id: int = None

    def __post_init__(self):
        """
        Post-initialization to validate the due date.
        """
        self._validate_due_date()

    def _validate_due_date(self):
        """
        Validates that the due date is not in the past.
        """
        if self.due_date < datetime.now():
            raise ValueError("Due date cannot be in the past.")

    @classmethod
    def from_dict(cls, data: dict):
        """
        To create a Task instance from a dictionary.
        """
        return cls(
            id=data.get("id"),
            task=data.get("task", ""),
            due_date=parse_to_datetime(data["due"]),
            created_at=data.get("created_at", datetime.now()),
            status=data.get("status", False),
        )

    def to_dict(self):
        """
        To create dictionary from Task Instance.
        """
        return {
            "_id": self.id,
            "task": self.task,
            "created_at": self.created_at,
            "due": to_datestr(str(self.due_date)),
            "status": self.status,
        }

    def get_task(self):
        """
        Get task description
        """
        return self.task

    def get_creation_date(self):
        """
        Get creation date
        """
        return self.created_at

    def get_due_date(self):
        """
        Get due date
        """
        return self.due_date

    def get_status(self):
        """
        Get task status
        """
        return self.status

    def __str__(self):
        """
        To print in str
        """
        return (
            f"Task(task='{self.task}',"
            f"due_date='{self.due_date.strftime(DD_MM_YYYY_HH_MM)}')"
        )
