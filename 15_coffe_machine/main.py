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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def coins():
    print("input money")
    money = int(input("how many quarters: ")) * 0.25
    money += int(input("how many dimes: ")) * 0.1
    money += int(input("how many nickels: ")) * 0.05
    money += int(input("how many pennies: ")) * 0.01
    return money

def check_resourses(sum_ingredients):
    for n in sum_ingredients:
        if sum_ingredients[n] >= resources[n]:
            print("cant make it")
            return 0
    return 1

income = 0
on = 1

while on:
    choice = input("what do you want? espresso, latte, cappucino: ")
    if choice == "off":
        on = 0
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffe: {resources['coffee']}g")
        print(f"money: ${income}")
    else:
        drink = MENU[choice]
        if check_resourses(drink["ingredients"]):
            pay = coins()
            if pay < drink["cost"]:
                print("no money")
            else:
                income = drink["cost"]
                print(f"Here is change: {round(pay - drink['cost'], 2)} and you {choice}")
                for n in drink["ingredients"]:
                    resources[n] -= drink["ingredients"][n]
 
            
            
        