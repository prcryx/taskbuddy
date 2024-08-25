from functools import wraps

import click
from taskbuddy.utils import db_status_file_exists


def validate_setup(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        # Check if the migration status file exists
        if not db_status_file_exists():
            click.echo(
                """Error: The setup has not been completed.
                Please run the `taskbuddy setup` command first."""
            )
            return
        return f(*args, **kwargs)

    return decorator
