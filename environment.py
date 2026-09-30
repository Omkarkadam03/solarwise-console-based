from config import *

def environmental(total_units):
    co2 = total_units * CO2_PER_UNIT
    trees = co2 / TREES_EQUIVALENT
    coal = total_units * COAL_PER_UNIT
    return co2, trees, coal