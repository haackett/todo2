from datetime import date



def get_distance(d0, d1):
    delta = d1 - d0
    return delta.days

def is_to_reccur(d0, d1, reccurenceInterval: int):
    dayDelta = get_distance(d0, d1)
    if dayDelta % reccurenceInterval == 0:
        return True
    else:
        return False