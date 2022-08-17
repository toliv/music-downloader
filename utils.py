from datetime import datetime


def string_of_date(dt: datetime) -> str:
    return '{0:%Y-%m-%d %H:%M:%S}'.format(dt)