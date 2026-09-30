def show_summary(capacity, total_cost, net_cost, total_savings, payback):
    print("\n💰 Financial Summary")
    print(f"Capacity: {round(capacity,2)} kW")
    print(f"Total Cost: ₹{round(total_cost)}")
    print(f"Net Cost: ₹{round(net_cost)}")
    print(f"Total Savings: ₹{round(total_savings)}")
    print(f"Payback Period: {round(payback,2)} years")


def show_environment(co2, trees, coal):
    print("\n🌍 Environmental Impact")
    print(f"CO2 Offset: {round(co2)} kg")
    print(f"Trees Equivalent: {round(trees)}")
    print(f"Coal Avoided: {round(coal,2)} tons")