from functools import wraps

import click

from taskbuddy.constants import DB_DIRNAME, MIGRATION_STATUS_FILENAME
from taskbuddy.utils import file_exists


def validate_setup(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        # Check if the migration status file exists
        if not file_exists(DB_DIRNAME, MIGRATION_STATUS_FILENAME):
            click.echo(
                """Error: The setup has not been completed.
                Please run the `taskbuddy setup` command first."""
            )
            return
        return f(*args, **kwargs)

    return decorator
