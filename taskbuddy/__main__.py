import click

from taskbuddy.types import Task
from taskbuddy.constants import DB_DIRNAME, MIGRATION_STATUS_FILENAME
from taskbuddy.decorators import validate_setup
from taskbuddy.migrations import run_migration
from taskbuddy.tasks_manager import create_task_manager
from taskbuddy.utils import print_header, file_exists


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = create_task_manager()


@cli.command()
@click.option("--db_path", default=None, help="setup database path")
def setup(db_path):
    """Setup the application (run migrations on first install)."""
    art = print_header()
    click.echo(art)
    if not file_exists(DB_DIRNAME, MIGRATION_STATUS_FILENAME):
        run_migration(db_path)
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


if __name__ == "__main__":
    cli()
