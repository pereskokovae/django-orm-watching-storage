SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600


def is_visit_long(visit, minutes=60):
    delta, _ = visit.get_duration()
    duration = delta.total_seconds() / SECONDS_IN_MINUTE
    return duration < minutes

def format_duration(visit):
    delta, _ = visit.get_duration()
    seconds = delta.total_seconds()
    hours = seconds // SECONDS_IN_MINUTE
    minutes = (seconds % SECONDS_IN_MINUTE) // SECONDS_IN_MINUTE
    return f"{int(hours)}ч {int(minutes):02d}мин"
