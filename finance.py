from config import COST_PER_KW

def calculate_financials(capacity, sector):
    total_cost = capacity * COST_PER_KW

    if sector == "residential":
        benefit = min(capacity * 30000, 78000)
    else:
        benefit = (total_cost * 0.40) * 0.30

    net_cost = total_cost - benefit
    return total_cost, benefit, net_cost