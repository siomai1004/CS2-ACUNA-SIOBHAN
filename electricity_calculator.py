# Electricity Bill Calculator
RATE = 12.90

# Validate customer's name
name = input("Enter customer name: ")

if name.strip() == "":
    print("Invalid name. PLease try again.")
    name = input("Enter customer name: ")
    
# Validate previous reading
previous = float(input("Enter previous meter reading: "))

if previous < 0:
    print("Invalid reading, please try again.")
    previous = float(input("Enter previous meter reading: "))
    
# Validate current reading    
current = float(input("Enter current meter reading: "))

if current < previous:
    print("Invalid reading, please try again")
    current = float(input("Enter current meter reading: "))

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))
