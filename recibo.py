import json

# Leer archivo JSON
with open('restaurante/menu.json', 'r') as archivo:
    options = json.load(archivo)

total_price = 0  # Variable para sumar los precios

# Función para mostrar platos y elegir uno
def show_and_select(category_index, category_name):
    print(f"{category_name}:")
    dishes = options["menu"][category_index]["dishes"]
    
    for idx, dish in enumerate(dishes, start=1):
        nom = dish["name"]
        ing = ", ".join(dish["ingredients"])
        pr = dish["price"]
        print(f"{idx}. {nom}")
        print(f"   Ingredients: {ing}")
        print(f"   Price: ${pr}\n")

    choice = int(input(f"What would you like for {category_name.lower()}? (write the number): "))
    selected_dish = dishes[choice - 1]
    return selected_dish["name"], selected_dish["price"]

# Selección de cada tipo de plato
appetizer, price1 = show_and_select(0, "Appetizers")
main_course, price2 = show_and_select(1, "Main Courses")
dessert, price3 = show_and_select(2, "Desserts")

# Total
total_price = price1 + price2 + price3

# Mostrar resumen
print("\nYour order summary:")
print(f"Appetizer: {appetizer} - ${price1}")
print(f"Main Course: {main_course} - ${price2}")
print(f"Dessert: {dessert} - ${price3}")
print(f"Total to pay: ${total_price}")


