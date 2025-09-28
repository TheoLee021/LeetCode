# Calculating the Length of a Time Period in Minutes
def time_period_length(time_period):
    start, end = (t.strip() for t in time_period.split("-"))
    
    hs, ms, ss = map(int, start.split(":"))
    he, me, se = map(int, end.split(":"))
    
    startMin = ((hs * 60) + ms)
    endMin = ((he * 60) + me)

    return endMin - startMin