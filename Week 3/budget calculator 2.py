
student_name = str(input("Student name: "))
transport = int(input("Daily Transport: "))
feeding = int(input("Daily Feeding: "))
days = int(input("Days spent in campus: "))
others = int(input("Other expenses: "))
budget = int(input("Budget: "))
transport_total = transport*days
feeding_total = feeding*days
total = transport_total+others+feeding_total

print()
print("==========Weekly Total==========")
print()
print(f"Student name: {student_name}")
print(f"Transport total: {transport_total}")
print(f"Feeding total: {feeding_total}")
print(f"Total: {total}")
if total < budget:
    print("Within Budget")
elif total == budget:
    print("Exactly Budget")
else:
    print("Above Budget")
print()
print("=================================")
