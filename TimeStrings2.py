# Parsing and Calculating Seconds from Time Strings in Python
def add_seconds_to_times(timePoints, seconds):
    # timeParts = [timePoint.split(":") for timePoint in timePoints]
    output = []
    DAY = 24 * 3600
    
    for timePoint in timePoints:
        # h = int(timePart[0])
        # m = int(timePart[1])
        # s = int(timePart[2])
        h, m, s = map(int, timePoint.split(":"))
        
        total = (h * 3600) + (m * 60) + s + seconds
        total %= DAY
        # totalSeconds = timePartSecond + seconds
        
        # h = totalSeconds // 3600
        # m = totalSeconds % 3600 // 60
        # s = totalSeconds % 3600 % 60
        h = total // 3600
        m = (total % 3600) // 60
        s = (total % 3600) % 60
        
        # timePart[0] = str(h)
        # timePart[1] = str(m)
        # timePart[2] = str(s)
        # ":".join(timePart) # need to store some where
        output.append(f"{h:02d}:{m:02d}:{s:02d}")
        
    return output