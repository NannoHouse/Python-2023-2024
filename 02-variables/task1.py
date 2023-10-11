def seconds_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secondss = seconds % 60
    return (hours, minutes,secondss)

