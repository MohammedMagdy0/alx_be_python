# shopping_list_manager.py

import os

FILENAME = "shopping_data.txt"

def file_exists_and_not_empty(filename):
    return os.path.isfile(filename) and os.path.getsize(filename) > 0

# ✅ تعريف القائمة بنفس النصوص المطلوبة
def display_menu():
    print("\nShopping List Manager")  # ✅ كما طلب التصحيح
    print("1. Add Item")              # ✅ كما طلب التصحيح
    print("2. Remove Item")
    print("3. View Shopping List")
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

def main():
    shopping_list = []

    if file_exists_and_not_empty(FILENAME):
        print(f"Note: '{FILENAME}' exists and is not empty.")

    while True:
        display_menu()
        choice_input = input("Enter your choice (1-4): ").strip()

        if not choice_input.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        
        choice = int(choice_input)

        if choice == 1:
            add_item(shopping_list)
        elif choice == 2:
            remove_item(shopping_list)
        elif choice == 3:
            view_list(shopping_list)
        elif choice == 4:
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

 
