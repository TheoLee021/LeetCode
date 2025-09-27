# Parsing and Calculating Seconds from Time Strings in Python
def solution(t, s):
    # chunk = t.split(":")
    time_part = [int(part) for part in t.split(":")]
    # hour = time_part[0]
    # minute = time_part[1]
    # second = time_part[2]
    seconds_since_start = time_part[0] * 3600 + time_part[1] * 60 + time_part[2]
    total_seconds = (seconds_since_start + s) % (24 * 3600) # The modulus operator (%) ensures that our total_seconds value doesn't exceed the total number of seconds in a day.

    # new_hour = int(hour) + s // 3600
    # new_minute = int(minute) + (s % 3600) // 60
    # new_second = int(second) + s % 60

    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"