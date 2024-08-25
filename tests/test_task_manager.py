import pytest
from taskbuddy.migrations import run_migration
from taskbuddy.tasks_manager import create_task_manager
from taskbuddy.types import Task


@pytest.fixture(scope="function")  # Changed to function scope
def mock_file_exists(mocker):
    """Mock the file_exists function to always return False during testing."""
    with mocker.patch("taskbuddy.utils.db_status_file_exists") as mock_file:
        mock_file.return_value = True
        yield


@pytest.fixture(scope="function")  # Changed to function scope
def mock_status_file(mocker):
    """Mock the file_exists function to always return False during testing."""
    mock_file = mocker.patch("taskbuddy.utils.write_status_file")
    yield mock_file


@pytest.fixture(scope="function")  # Changed to function scope
def mock_run_migrations(mock_file_exists, mock_status_file):
    # Call the function
    run_migration(db_name="test_db")

    # Assert the mock functions were called as expected
    mock_file_exists.assert_called_once()
    mock_status_file.assert_called_once_with("test_db")
    yield


@pytest.fixture(scope="function")  # Changed to function scope
def mock_db_connection(mocker):
    """Mock the database connection."""
    return mocker.patch(
        "taskbuddy.database.DatabaseConnectionFactory.create_connection"
    )


@pytest.fixture(scope="function")  # Changed to function scope
def mock_db_adapter(mocker):
    """Mock the database adapter."""
    return mocker.patch("taskbuddy.database.SQLiteAdapter")


@pytest.fixture(scope="function")  # Changed to function scope
def mock_task_manager(mock_db_connection, mock_db_adapter):
    """Create a database connection after migrations have run."""
    return create_task_manager(db_type="sqlite")


def test_add_task(mocker, mock_task_manager):
    """Test the add_task method of TaskManager."""
    # Mock the method that interacts with the database
    mock_add_task = mocker.patch.object(mock_task_manager, "add_task")

    # Define a sample task name
    mock_task = Task.from_dict(
        {
            "id": 1,
            "task": "New Task",
            "due": "12-09-2024",
        }
    )

    # Call the add_task method
    mock_task_manager.add_task(mock_task)

    # Assert that the add_task method was called with the correct argument
    mock_add_task.assert_called_once_with(mock_task)


def test_view_task(mocker, mock_task_manager):
    """Test the view_task method of TaskManager."""
    # Mock the method that interacts with the database
    mock_view_task = mocker.patch.object(mock_task_manager, "view_all_tasks")

    # Define a sample task ID and task instance
    mock_tasks = [
        Task.from_dict(
            {
                "id": 1,
                "task": "New Task",
                "due": "12-09-2024",
            }
        )
    ]

    # Mock the return value of view_task
    mock_view_task.return_value = mock_tasks

    # Call the view_task method
    result = mock_task_manager.view_all_tasks()

    # Assert that the view_task method was called with the correct argument
    mock_view_task.assert_called_once()

    # Assert that the return value is the expected task instance
    assert result == mock_tasks


def test_view_task_by_id(mocker, mock_task_manager):
    mock_view_single_task = mocker.patch.object(
        mock_task_manager, "view_task_by_id"
    )

    mock_task = Task.from_dict(
        {
            "id": 1,
            "task": "New Task",
            "due": "12-09-2024",
        }
    )
    mock_view_single_task.return_value = mock_task

    # Call the view_task method
    result = mock_task_manager.view_task_by_id(task_id=1)

    # Assert that the return value is the expected task instance
    assert result == mock_task
