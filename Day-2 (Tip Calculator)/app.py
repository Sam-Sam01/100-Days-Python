print("Welcome to the Tip Calculator.")
total_bill = int(input("What was the total bill?\n"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill into?"))
one_person_pay = (total_bill*(percentage/100)+total_bill)/people
print(f"One person's bill is: {one_person_pay}")