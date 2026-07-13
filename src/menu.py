def run_menu():
    while True:
        print("\nAI Ticket Analyzer")
        print("1. Create ticket")
        print("2. List tickets")
        print("3. Search ticket")
        print("4. Update ticket")
        print("5. Close ticket")
        print("6. Delete ticket")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Create ticket selected")
        elif choice == "2":
            print("List tickets selected")
        elif choice == "3":
            print("Search ticket selected")
        elif choice == "4":
            print("Update ticket selected")
        elif choice == "5":
            print("Close ticket selected")
        elif choice == "6":
            print("Delete ticket selected")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
