def is_visit_long(visit, minutes=60):
    delta, _, _ = visit.get_duration()
    duration = delta.total_seconds() / 60
    return duration < minutes

def format_duration(visit):
    delta, _, _ = visit.get_duration()
    seconds = delta.total_seconds()
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{int(hours)}ч {int(minutes)}мин"