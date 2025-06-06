

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            def add_item(item):
                shopping_list.append(item)
            item = input("Enter the item to add: ")
            add_item(item)
        elif choice == '2':
            def remove_item(item):
                if item in shopping_list:
                    shopping_list.remove(item)
                else:
                    print(f"Item '{item}' not found in the shopping list.")

            item = input("Enter the item to remove: ")
            remove_item(item)
        elif choice == '3':
            def view_items():
                if not shopping_list:
                    print("Shopping list is empty.")
                for item in shopping_list:
                    print(f"- {item}")

            view_items()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




