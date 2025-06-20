breakfast = {
    "upma":50,
    "poha":70,
    "sandwitch":80,
    "bead butter":50,

}

lunch = {
    "idli":50,
    "vada":40,
    "chole bhature":70,
    "rajma chawal":60,
    "pulao":70,
    "pizza":90,
}

dinner = {
    "biryani":100,
    "chicken tikka":120,
    "pulao":100,
    "kabab seekh":90,
    "dal makhani":80,
    "paneer tikka":100,
    "chicken curry":120,
    "mutton curry":150,
    "dal tadka":70,
    "dal fry":70,
    "dal palak":80,
}

drinks = {
    "tea":10,
    "coffee":20,
    "cold drink":30,
    "juice":40,
    "milkshake":50,
    "lassi":30,
}
print("------------------------------------------------------------------------------")
print("WELCOME TO OUR CAFE ☕\n ")
print("------------------------------------------------------------------------------\n")
print("WE SERVE : \n 1)breakfast 🥞\n 2)lunch 🍴\n 3)dinner 🍽️\n 4)drinks 🍷.")

meal_type = input("Please select a meal type:").strip().lower()
if meal_type == "breakfast"or meal_type == "1":
    print("------------------------------------------------------------------------------\n")
    print("Breakfast Menu: 🥞\n")
    for item, price in breakfast.items():
        print(f"{item}: ₹{price}")
    print("------------------------------------------------------------------------------\n") 

elif meal_type == "lunch" or meal_type == "2":
    print("------------------------------------------------------------------------------\n") 
    print("Lunch Menu:🍴\n")
    for item, price in lunch.items():
        print(f"{item}: ₹{price}")
    print("------------------------------------------------------------------------------\n") 

elif meal_type == "dinner" or meal_type == "3":
    print("------------------------------------------------------------------------------\n") 
    print("Dinner Menu:🍽️\n")
    for item, price in dinner.items():
        print(f"{item}: ₹{price}")
    print("------------------------------------------------------------------------------\n") 

elif meal_type == "drinks" or meal_type == "4":
    print("------------------------------------------------------------------------------\n")   
    print("Drinks Menu:🍷\n")
    for item, price in drinks.items():
        print(f"{item}: ₹{price}")
    print("------------------------------------------------------------------------------\n")
else:
    print("Invalid meal type selected. Please try again.")
    exit()

order = input("Please enter your order  ").lower()
order_total = 0
if order in breakfast:
    order_total += breakfast[order]
elif order in lunch:
    order_total += lunch[order] 
elif order in dinner:
    order_total += dinner[order]
elif order in drinks:
    order_total += drinks[order]
else:
    print("Invalid order. Please try again.")
    exit()

print(f"Your order: {order} - ₹{order_total} \n")
print("------------------------------------------------------------------------------")
print("Your order has been placed successfully! 🎉\n")
order_2 = input("Would you like to order another item? (yes/no): ").strip().lower()
if order_2 == "yes":
    additional_order = input("Please enter your additional order: ").lower()
    if additional_order in breakfast:
        order_total += breakfast[additional_order]
    elif additional_order in lunch:
        order_total += lunch[additional_order]
    elif additional_order in dinner:
        order_total += dinner[additional_order]
    elif additional_order in drinks:
        order_total += drinks[additional_order]
    else:
        print("Invalid order. Please try again.")
    print(f"Your updated order: {order}+{additional_order} - ₹{order_total}")

print("Thank you for your order! Enjoy your meal! 🍽️")