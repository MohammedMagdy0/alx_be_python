
def display_menu():
    print("\n--- Shopping List Manager ---")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View shopping list")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the item to add: ").strip()
    shopping_list.append(item)
    print(f"'{item}' has been added to your shopping list.")

def remove_item(shopping_list):
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
    else:
        print(f"'{item}' is not in your shopping list.")

def view_list(shopping_list):
    if shopping_list:
        print("\nYour Shopping List:")
        for idx, item in enumerate(shopping_list, 1):
            print(f"{idx}. {item}")
    else:
        print("Your shopping list is currently empty.")
