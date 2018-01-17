def minutes_to_hours(seconds, minutes = 60):
    hours = minutes / 60 + seconds / 3600
    return hours

print(minutes_to_hours(300, 100))
