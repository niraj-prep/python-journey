# Employee Information and Salary Calculator

name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
department = input("Enter Department: ")
basic_salary = float(input("Enter Basic Salary: "))

da  = 0.92 * basic_salary
hra = 0.58 * basic_salary
ta  = 0.30 * basic_salary
lic = 500

gross_salary = basic_salary + da + hra + ta
net_salary   = gross_salary - lic

print("\n--- Employee Salary Details ---")
print(f"Name       : {name}")
print(f"Employee ID: {emp_id}")
print(f"Department : {department}")
print(f"Basic Salary : Rs. {basic_salary:.2f}")
print(f"DA (92%)     : Rs. {da:.2f}")
print(f"HRA (58%)    : Rs. {hra:.2f}")
print(f"TA (30%)     : Rs. {ta:.2f}")
print(f"Gross Salary : Rs. {gross_salary:.2f}")
print(f"LIC Deduction: Rs. {lic:.2f}")
print(f"Net Salary   : Rs. {net_salary:.2f}")