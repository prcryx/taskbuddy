import click
import shutil
from taskbuddy.types import Task
from taskbuddy.decorators import validate_setup
from taskbuddy.migrations import run_migration
from taskbuddy.tasks_manager import TaskManager, create_task_manager
from taskbuddy.utils import print_header, db_status_file_exists


@click.group()
@click.pass_context
def cli(ctx):
    if not db_status_file_exists():
        return
    ctx.obj = create_task_manager()


@cli.command()
@click.option("--db_name", default=None, help="setup database path")
def setup(db_name):
    """Set up the application (run migrations on first install)."""
    art = print_header()
    click.echo(art)
    if not db_status_file_exists():
        run_migration(db_name)
    else:
        click.echo("Setup has already been completed.")


# Add Task Functionality
@cli.command(name="add")
@click.option(
    "--task",
    "task_description",
    required=True,
    help="Description of the task.",
)
@click.option(
    "--due",
    "due_date",
    required=True,
    help="Due date of the task in DD-MM-YYY format.",
)
@click.pass_context
@validate_setup
def add(ctx, task_description, due_date):
    """Add new task."""
    try:
        task = Task.from_dict({"task": task_description, "due": due_date})

        # Retrieve the TaskManager from the context and add the task
        task_manager = ctx.obj
        task_manager.add_task(task)
        click.echo(f"Task added: {task}")

    except ValueError as e:
        click.echo(f"Error: {str(e)}")


# View All Task Functionality
@cli.command(name="ls")
@click.option("--all", "list_all", is_flag=True, required=True)
@click.pass_context
@validate_setup
def list_tasks(ctx, list_all: bool):
    """List tasks."""
    task_manager: TaskManager = ctx.obj
    if list_all:
        tasks: [Task] = task_manager.view_all_tasks()
        for task in tasks:
            print_task(task)
    else:
        click.echo("Please specify --all to list all task.")


# print task
def print_task(task: Task):
    terminal_width = shutil.get_terminal_size().columns
    click.echo(task.to_dict())
    click.echo("-" * terminal_width)


if __name__ == "__main__":
    cli()
