from config import SUN_HOURS, EFFICIENCY

def auto_size():
    bill = float(input("Monthly Bill (₹): "))
    tariff = float(input("Tariff (₹/unit): "))

    daily_units = (bill / tariff) / 30
    capacity = daily_units / (SUN_HOURS * EFFICIENCY)

    print(f"Recommended Capacity: {round(capacity,2)} kW")
    return capacity, tariff


def manual_mode():
    capacity = float(input("Enter Capacity (kW): "))
    tariff = float(input("Enter Tariff (₹/unit): "))
    return capacity, tariff