print("Welcome to Pizzazz!")
size = input("What size pizza you want to serve? S, M or L")
add_pepperoni = input("Do you want pepperoni? (y/n): ")
add_cheese = input("Do you want extra cheese? (y/n): ")
size = size.upper()
add_cheese = add_cheese.upper()
add_pepperoni = add_pepperoni.upper()
bill = 0

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

    if add_pepperoni == "Y":
        bill += 3
    if add_cheese == "Y":
        bill += 1

print("Your total bill is: $", bill)