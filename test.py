def add_seconds_to_times(timePoints, seconds):
    output = []
    
    for timePoint in timePoints:
        h, m, s = map(int, timePoint.split(":"))
        
        total = (h * 3600) + (m * 60) + s + seconds
        total %= 24 * 3600
        
        h, remainder = divmod(total, 3600)
        m, s = divmod(remainder, 60)
        
        output.append(f"{h:02d}:{m:02d}:{s:02d}")
    
    return output
    
print(add_seconds_to_times(['10:00:00', '23:30:00'], 3600))