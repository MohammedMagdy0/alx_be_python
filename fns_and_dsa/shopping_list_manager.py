# shopping_list_manager.py

import os

# Optional: Check if a file exists (future use for loading/saving)
FILENAME = "shopping_data.txt"

def file_exists_and_not_empty(filename):
    return os.path.isfile(filename) and os.path.getsize(filename) > 0

# ✅ تعريف دالة عرض القائمة
def display_menu():
    print("\n--- Shopping List Manager ---")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View shopping list")
    print("4. Exit")

# ✅ دوال الإضافة والحذف والعرض
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

# ✅ البرنامج الرئيسي
def main():
    # ✅ إنشاء القائمة
    shopping_list = []

    # Optional: File check
    if file_exists_and_not_empty(FILENAME):
        print(f"Note: '{FILENAME}' exists and is not empty. (This is just a check for now)")

    while True:
        # ✅ استدعاء الدالة كل مرة
        display_menu()
        choice_input = input("Enter your choice (1-4): ").strip()

        # ✅ تأكد من أن الإدخال رقم
        if not choice_input.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        
        choice = int(choice_input)

        # ✅ تنفيذ الاختيارات
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

# ✅ نقطة التشغيل الرئيسية
if __name__ == "__main__":
    main()

