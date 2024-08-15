import click

# from taskbuddy.migrations import , tasks
from taskbuddy.constants import DB_DIRNAME, MIGRATION_STATUS_FILENAME
from taskbuddy.utils import get_default_db_path, print_header, file_exists
from taskbuddy.migrations import run_migration

DEFAULT_DB_PATH = get_default_db_path()


@click.group()
def cli():
    pass


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


if __name__ == "__main__":
    cli()
