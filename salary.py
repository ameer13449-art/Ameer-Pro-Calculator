# Smart Calc & Payroll System
# Created by: Ameer

print("--- Smart Payroll System (Tax Rules) ---")

name = input("Enter Employee Name: ")
basic = float(input("Enter Basic Salary ($): "))
allowance = float(input("Enter Allowance ($): "))

# إجمالي الراتب
gross_salary = basic + allowance

# القاعدة الذكية للضريبة
if gross_salary > 1000:
    tax_rate = 0.10  # خصم 10% للرواتب العالية
    tax_note = "Tax Applied (High Salary)"
else:
    tax_rate = 0.00  # لا يوجد خصم
    tax_note = "No Tax (Support Level)"

tax_amount = gross_salary * tax_rate
net_salary = gross_salary - tax_amount

print("\n" + "="*35)
print(f"Employee Name: {name}")
print(f"Gross Salary: ${gross_salary}")
print(f"Status: {tax_note}")
print(f"Tax Amount: -${tax_amount}")
print(f"Net Salary to Pay: ${net_salary}")
print("="*35)
print("System by: Ameer")
