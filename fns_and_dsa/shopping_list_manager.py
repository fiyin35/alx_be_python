# Author: Fiyinfolu
# shopping list manager is a script
# to manage user shopping list by 
# displaying the menu options for 
# user to add, remove or display the 
# shopping list
# add_item function is to add items to the shopping list
# remove_item function is to remove items from the shopping list
# list_items function is to display items in the shopping list


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4 Exit")

def add_item(item, shopping_list):
    shopping_list.append(item)
    print(f"{item} added to the list successfully")

def remove_item(item, shopping_list):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the list successfully")
    else:
        print(f"{item} does not exist in the Shopping List")
def list_item(item, shopping_list):
    if len(shopping_list) == 0:
        print("Shopping List is empty")
    else:
        for item in shopping_list:
            print(item)




def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ").strip().capitalize()
            add_item(item, shopping_list)
        elif choice == '2':
            item = input("Enter the item you want to remove: ").strip().capitalize()
            remove_item(item, shopping_list)        
        elif choice == '3':
            list_item(item, shopping_list)
        elif choice == '4':
            print("Goodbye, it was nice having you!!")
            break 
        else:
            print("Invalid choice, Please try again")

if __name__ == '__main__':
    main()


