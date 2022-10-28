from random import random

# Define function to bin column values.
def bin_values(revenue, v):
    if revenue >= v:
        val = 1
    elif revenue < v:
        val = 0
    else:
        val = revenue
    return val

def mock_drift(v, drift_threshold):
    if random() < drift_threshold:
        return v * 1.25
    else:
        return v
