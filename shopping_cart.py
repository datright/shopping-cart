products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

import datetime

e = datetime.datetime.now()

# 1. Capture and validate user selections
total_price = 0
selected_ids = []
valid_ids = []

for p in products:
    valid_ids.append(p["id"])

while True:
    selected_id = input("Please input a product identifier or DONE when you are done:") #> string
    if selected_id == "DONE":
        break
    elif float(selected_id) not in valid_ids: 
        print("Invalid input. Please try again.")
    else:
        selected_ids.append(selected_id)
#print(selected_id)
#print(type(selected_id))
        #matching_products = [p for p in products if p["id"] == float(selected_id)]
        #matching_product = matching_products[0]
        #otal_price = total_price + matching_product["price"]
        #print("Selected Product:", matching_product["name"],"",str(matching_product["price"]))

#print(matching_product)
#print(type(matching_product))

# 2. Info Display 
print("-----------------------")
print("DAT ORGANIC GROCERY")
print("WWW.DATORGANIC.COM")
print("-----------------------")

print ("Checkout time at:", e.strftime("%d/%m/%Y"), e.strftime("%I:%M:%S %p"))

print("-----------------------")
print("Selected Products:")

#print(selected_ids)

for selected_id in selected_ids:
    matching_products = [p for p in products if p["id"] == float(selected_id)]
    matching_product = matching_products[0]
    total_price = total_price + matching_product["price"]
    for p in matching_products:
        print("...", p["name"],"", to_usd(float(p["price"])))

print("-----------------------")


print("Subtotal:", to_usd(float(total_price)))

tax = total_price * 0.0875
print("Tax:", to_usd(tax))
total = total_price + tax
print("Total:", to_usd(total))

print("-----------------------")
print("THANK YOU! SEE YOU AGAIN SOON!")
print("-----------------------")
