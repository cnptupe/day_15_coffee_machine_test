MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}

coffee_machine_resources = resources
coffee_machine_resources['money'] = 0.0

# 3. When "report" is entered on the prompt then it should show available resources and revenue.
def print_report():
    """When "report" is entered on the prompt then it should print available resources and revenue.
    """
    water_qty =  coffee_machine_resources['water']
    milk_qty = coffee_machine_resources['milk']
    coffee_qty = coffee_machine_resources['coffee']
    money_amount = coffee_machine_resources['money']
    print(f"Water: {water_qty}ml\n"
          f"Milk: {milk_qty}ml\n"
          f"Coffee: {coffee_qty}g\n"
          f"Money: ${money_amount}\n")

# 7. Make coffee
def make_coffee(usr_choice):
    print(f"Here's your {usr_choice} ☕. Enjoy!")
    #Update coffee resources in the coffee machine
    coffee_machine_resources['water'] -= MENU[usr_choice]['ingredients']['water']
    coffee_machine_resources['coffee'] -= MENU[usr_choice]['ingredients']['coffee']
    if usr_choice != "espresso":
        coffee_machine_resources['milk'] -= MENU[usr_choice]['ingredients']['milk']

    #Update amount in the coffee machine
    coffee_machine_resources['money'] += MENU[usr_choice]['cost']


# 4. Check resources before any transaction.
def check_coffee_resources_ok(usr_choice):
    global MENU
    if coffee_machine_resources['water'] < MENU[usr_choice]['ingredients']['water']:
        print("Sorry there is not enough water.")
        return False
    elif coffee_machine_resources['coffee'] < MENU[usr_choice]['ingredients']['coffee']:
        print("Sorry there is not enough coffee.")
        return False
    elif usr_choice != "espresso":
        if coffee_machine_resources['milk'] < MENU[usr_choice]['ingredients']['milk']:
            print("Sorry there is not enough milk.")
            return False
        else:
            return True
    else:
        return True

def calculate_amount(quarters_qty, dimes_qty, nickles_qty, pennies_qty):
    return quarters_qty * .25 + dimes_qty * .1 + nickles_qty * .05 + pennies_qty * .01

# 5. Process coins to get how much money has been received.
def insert_coins():
    print("Please insert coins.")
    quarters_qty = int(input("how many quarters?: "))
    dimes_qty = int(input("how many dimes?: "))
    nickles_qty = int(input("how many nickles?: "))
    pennies_qty = int(input("how many pennies?: "))
    money_inserted = calculate_amount(quarters_qty, dimes_qty, nickles_qty, pennies_qty)
    return money_inserted
    # print("Sorry that's not enough money. Money refunded.")

# 6. Check if the transaction is successful - inserted enough money, not enough money, change
def check_transaction(money_inserted, usr_choice):
    if MENU[usr_choice]['cost'] <= money_inserted:
        change_money = round(money_inserted - MENU[usr_choice]['cost'], 2)
        if change_money > 0:
            print(f"Here is ${change_money} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def serve_coffee(usr_choice):
    if usr_choice == "report":
        print_report()
    elif usr_choice == "espresso" or "latte" or "cappuccino":
        if check_coffee_resources_ok(usr_choice):
            money_inserted = insert_coins()
            if check_transaction(money_inserted, usr_choice):
                make_coffee(usr_choice)

serving_coffee = True
while serving_coffee:
    # 1. Create a Running Prompt which always listens
    user_choice = input("What would you like? (espresso-$1.5/latte-$2.5/cappuccino-$3.0): ").lower()

    # 2. When "off" is entered on the prompt program should exit
    if user_choice == "off":
        print("Taking service down for maintenance.")
        serving_coffee = False
    else:
        serve_coffee(user_choice)



