def check_eligibility():
    print("\n--- Eligibility Check ---")
    citizen = input("Citizen? (yes/no): ").lower()
    roof = input("Roof Rights? (yes/no): ").lower()
    return citizen == "yes" and roof == "yes"