from eligibility import check_eligibility
from input_handler import auto_size, manual_mode
from finance import calculate_financials
from simulation import simulate
from environment import environmental
from display import show_summary, show_environment
from session import save_session, show_comparison

def main():
    print("\n🌱 SOLARWISE SYSTEM 🌱")

    while True:
        if not check_eligibility():
            print("❌ Not Eligible\n")
            continue

        sector = input("Sector (residential/commercial): ").lower()

        print("\n1. Auto-Sizer\n2. Manual")
        mode = input("Select Mode: ")

        if mode == "1":
            capacity, tariff = auto_size()
        else:
            capacity, tariff = manual_mode()

        total_cost, benefit, net_cost = calculate_financials(capacity, sector)

        table, total_units, total_savings = simulate(capacity, tariff)

        co2, trees, coal = environmental(total_units)

        first_year_savings = capacity * 365 * 5 * 0.8 * tariff
        payback = net_cost / first_year_savings

        print("\n📊 25-Year Projection")
        print(table)

        show_summary(capacity, total_cost, net_cost, total_savings, payback)
        show_environment(co2, trees, coal)

        save_session({
            "capacity": round(capacity,2),
            "sector": sector,
            "net_cost": round(net_cost),
            "savings": round(total_savings),
            "payback": round(payback,2),
            "co2": round(co2)
        })

        again = input("\nRun another scenario? (yes/no): ").lower()
        if again != "yes":
            break

    show_comparison()
    print("\n✅ End of Analysis")


if __name__ == "__main__":
    main()