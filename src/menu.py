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


def get_ticket_index(action):
    if not tickets:
        print("No tickets found.")
        return None

    try:
        ticket_number = int(input(f"Ticket number to {action}: "))
    except ValueError:
        print("Invalid ticket number. Please enter a number.")
        return None

    ticket_index = ticket_number - 1

    if ticket_index < 0 or ticket_index >= len(tickets):
        print("Invalid ticket number.")
        return None

    return ticket_index


def list_tickets():
    if not tickets:
        print("No tickets found.")
        return

    for index, ticket in enumerate(tickets, start=1):
        display_ticket(ticket, index)


def search_tickets():
    if not tickets:
        print("No tickets found.")
        return

    search_term = input("Search term: ").lower()
    found_tickets = []

    for ticket in tickets:
        title = ticket["title"].lower()
        description = ticket["description"].lower()

        if search_term in title or search_term in description:
            found_tickets.append(ticket)

    if not found_tickets:
        print("No matching tickets found.")
        return

    for index, ticket in enumerate(found_tickets, start=1):
        display_ticket(ticket, index)


def close_ticket():
    ticket_index = get_ticket_index("close")

    if ticket_index is None:
        return

    selected_ticket = tickets[ticket_index]
    selected_ticket["status"] = "closed"
    print("Ticket closed successfully.")


def delete_ticket():
    ticket_index = get_ticket_index("delete")

    if ticket_index is None:
        return

    deleted_ticket = tickets.pop(ticket_index)
    print(f"Ticket deleted successfully: {deleted_ticket['title']}")


def update_ticket():
    ticket_index = get_ticket_index("update")

    if ticket_index is None:
        return

    selected_ticket = tickets[ticket_index]

    print("Press Enter to keep the current value.")
    title = input(f"Title [{selected_ticket['title']}]: ")
    description = input(f"Description [{selected_ticket['description']}]: ")
    category = input(f"Category [{selected_ticket['category']}]: ")
    priority = input(f"Priority [{selected_ticket['priority']}]: ")
    status = input(f"Status [{selected_ticket['status']}]: ")

    if title:
        selected_ticket["title"] = title
    if description:
        selected_ticket["description"] = description
    if category:
        selected_ticket["category"] = category
    if priority:
        selected_ticket["priority"] = priority
    if status:
        selected_ticket["status"] = status

    print("\nTicket updated successfully!")
    display_ticket(selected_ticket, ticket_index + 1)


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
            update_ticket()
        elif choice == "5":
            close_ticket()
        elif choice == "6":
            delete_ticket()
        elif choice == "0":
            print("Goodbye!")
            break
