from linked_list import LinkedList, OutOfRangeError, UnderflowError

l_list = LinkedList()

print("\n===== Welcome to Linked List program =====\n")
print("1. Add a node.")
print("2. Print the list.")
print("3. Delete a node.")
print("4. Exit")

while True:
    choice = int(input("\nEnter your choice: "))

    match choice:
        case 1:
            value = input("Enter the value to add: ")
            l_list.add(value)

        case 2:
            try:
                l_list.print_list()
            except UnderflowError as err:
                print(f"UnderflowError: {err}")

        case 3:
            n = int(input("Enter the position to delete: "))
            try:
                l_list.delete(n)
            except UnderflowError as err:
                print(f"UnderflowError: {err}")
            except OutOfRangeError as err:
                print(f"OutOfRangeError: {err}")

        case 4:
            print("Terminating all operations...\n")
            break

        case _:
            print("Wrong choice.")
