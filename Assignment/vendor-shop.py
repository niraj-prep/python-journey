# Vendor Details and Annual Purchase Report

name = input("Enter Vendor Name: ")
year = input("Enter Year of Association: ")
contact = input("Enter Contact Number: ")
email = input("Enter eMail ID: ")

total = 0
print("\nEnter monthly purchase amounts:")
months = ["Jan","Feb","Mar","Apr","May","Jun",
          "Jul","Aug","Sep","Oct","Nov","Dec"]

monthly = []
for m in months:
    amt = float(input(f"  {m}: Rs. "))
    monthly.append(amt)
    total += amt

print("\n--- Annual Purchase/Billing Report ---")
print(f"Vendor Name       : {name}")
print(f"Year of Association: {year}")
print(f"Contact Number    : {contact}")
print(f"eMail ID          : {email}")
print("\nMonthly Purchases:")
for m, a in zip(months, monthly):
    print(f"  {m}: Rs. {a:.2f}")
print(f"\nTotal Annual Purchase: Rs. {total:.2f}")