MATCH = 1
MISMATCH = -1
GAP = -2

def score(a, b):
    if a == b:
        return MATCH
    else:
        return MISMATCH
    
    