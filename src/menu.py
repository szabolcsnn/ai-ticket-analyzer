MENU_OPTIONS = {
    "1": "Create ticket",
    "2": "List tickets",
    "3": "Search ticket",
    "4": "Update ticket",
    "5": "Close ticket",
    "6": "Delete ticket",
    "0": "Exit",
}

tickets = []


def create_ticket():
    title = input("Title: ")
    description = input("Description: ")
    category = input("Category: ")
    priority = input("Priority: ")
    status = "open"

    ticket = {
        "title": title,
        "description": description,
        "category": category,
        "priority": priority,
        "status": status,
    }

    tickets.append(ticket)

    print("\nTicket created successfully!")
    print(f"Title: {title}")
    print(f"Description: {description}")
    print(f"Category: {category}")
    print(f"Priority: {priority}")
    print(f"Status: {status}")


def display_ticket(ticket, index):
    print(f"\nTicket #{index}")
    print(f"Title: {ticket['title']}")
    print(f"Description: {ticket['description']}")
    print(f"Category: {ticket['category']}")
    print(f"Priority: {ticket['priority']}")
    print(f"Status: {ticket['status']}")


def list_tickets():
    if not tickets:
        print("No tickets found")
        return

    for index, ticket in enumerate(tickets, start=1):
        display_ticket(ticket, index)


def search_tickets():
    if not tickets:
        print("No tickets found")
        return

    search_term = input("Search term: ").lower()
    found_tickets = []

    for ticket in tickets:
        title = ticket["title"].lower()
        description = ticket["description"].lower()

        if search_term in title or search_term in description:
            found_tickets.append(ticket)

    if not found_tickets:
        print("No matching tickets found")
        return

    for index, ticket in enumerate(found_tickets, start=1):
        display_ticket(ticket, index)


def run_menu():
    while True:
        print("\nAI Ticket Analyzer")

        for option_number, option_label in MENU_OPTIONS.items():
            print(f"{option_number}. {option_label}")

        choice = input("Choose an option: ")

        if choice not in MENU_OPTIONS:
            print("Invalid option. Please try again.")
            continue

        if choice == "1":
            create_ticket()
        elif choice == "2":
            list_tickets()
        elif choice == "3":
            search_tickets()
        elif choice == "4":
            print("Update ticket selected")
        elif choice == "5":
            print("Close ticket selected")
        elif choice == "6":
            print("Delete ticket selected")
        elif choice == "0":
            print("Goodbye!")
            break
