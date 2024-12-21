from database import ingredients, coffee_prices, sales_report

def make_coffee(coffee_type):
    coffee_requirements ={
        "latte" : {"water" : 200, "milk" : 150, "coffee" : 24},
        "cappuccino" : {"water" : 250, "milk": 100, "coffee" :24},
        "americano" : {"water" : 250, "milk": 0, "coffee" : 20}
    }

    if all(ingredients[ingredient] >= coffee_requirements[coffee_type][ingredient] for ingredient in coffee_requirements[coffee_type]):
    # Deduct the required ingredients
        for ingredient in coffee_requirements[coffee_type]:
            ingredients[ingredient] -= coffee_requirements[coffee_type][ingredient]

        
        sales_report[coffee_type] += 1
        sales_report["total_money"] += coffee_prices[coffee_type]

        print(f"Making {coffee_type} coffee...    Enjoy!")
    else:
        print(f"Sorry, we don't have enough ingredients to make a {coffee_type}.")


def process_payment(coffee_type):
    price = coffee_prices[coffee_type]
    total_money_inserted = 0
    money_inserted = 0
    while total_money_inserted < price:
        money_inserted += float(input(f"Please insert ${price} or more: "))
        if money_inserted in [1, 2, 5]:
            total_money_inserted += money_inserted
            print(f"Total money iserted: ${total_money_inserted}")
        else:
            print("Invalid input, please insert a valid coin.")

    if total_money_inserted >= price:
        change = total_money_inserted - price
        if change > 0:
            print(f"Here's your change: ${change}")
        return True
    else:
        print("Insufficient funds. Please insert more money.")  
        return False 
    

def show_status():
    print("Ingredients:")
    for ingredient, amount in ingredients.items():
        print(f"{ingredient}: {amount} ml")
    
    print("\nSales report:")
    for coffee_type, sales in sales_report.items():
        if coffee_type != "total_money":
            print(f"{coffee_type.capitalize()}: {sales} sold")
    print(f"Total money collected: ${sales_report["total_money"]}")
        

def main():
    while True:
        print("\nWelcome to the Coffee Shop!")
        
        coffee_choice = input("What type of coffee would you like? (Latte, Cappuccino, Americano): ").lower().strip()

        if coffee_choice == "off":
            print("Turning off the coffee machine!")
            break
        elif coffee_choice == "status":
            show_status()
        elif coffee_choice in coffee_prices:
            if process_payment(coffee_choice):
                make_coffee(coffee_choice)
        else:
            print("Invalid choice. Please try again.")

main()