from prettytable import PrettyTable
from config import *

def simulate(capacity, tariff):
    generation = capacity * DAYS * SUN_HOURS * EFFICIENCY

    table = PrettyTable()
    table.field_names = ["Year", "Units", "Tariff", "Savings"]

    total_units = 0
    total_savings = 0

    for year in range(1, YEARS + 1):
        savings = generation * tariff

        table.add_row([
            year,
            round(generation, 2),
            round(tariff, 2),
            round(savings, 2)
        ])

        total_units += generation
        total_savings += savings

        generation *= (1 - DEGRADATION)
        tariff *= (1 + TARIFF_GROWTH)

    return table, total_units, total_savings