from finance_tools.tax import calculate_tax
from finance_tools.loan import calculate_emi


print("===== Finance App =====")

# Tax
income = float(input("Enter your annual income: "))
tax_rate = float(input("Enter tax rate (%): "))

tax = calculate_tax(income, tax_rate)

print(f"Calculated Tax: {tax:.2f}")


# Loan
principal = float(input("\nEnter loan amount: "))
annual_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter loan period (years): "))

emi = calculate_emi(principal, annual_rate, years)

print(f"Monthly EMI: {emi:.2f}")