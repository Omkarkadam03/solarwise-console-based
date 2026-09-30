from prettytable import PrettyTable

sessions = []

def save_session(data):
    sessions.append(data)

def show_comparison():
    print("\n📊 FINAL COMPARISON")

    table = PrettyTable()
    table.field_names = ["Sr. No.", "kW", "Sector", "Net Cost", "Savings", "Payback", "CO2"]

    for i, s in enumerate(sessions, 1):
        table.add_row([
            i,
            s["capacity"],
            s["sector"],
            s["net_cost"],
            s["savings"],
            s["payback"],
            s["co2"]
        ])

    print(table)