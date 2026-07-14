from src.ticket_service import TicketService


MENU_OPTIONS = {
    "1": "Create ticket",
    "2": "List tickets",
    "3": "Search ticket",
    "4": "Update ticket",
    "5": "Close ticket",
    "6": "Delete ticket",
    "0": "Exit",
}


def create_ticket(ticket_service):
    title = input("Title: ")
    description = input("Description: ")
    category = input("Category: ")
    priority = input("Priority: ")

    ticket = ticket_service.create_ticket(
        title=title,
        description=description,
        category=category,
        priority=priority,
    )

    print("\nTicket created successfully!")
    display_ticket(ticket, ticket_service.ticket_count())


def display_ticket(ticket, index):
    print(f"\nTicket #{index}")
    print(f"Title: {ticket.title}")
    print(f"Description: {ticket.description}")
    print(f"Category: {ticket.category}")
    print(f"Priority: {ticket.priority}")
    print(f"Status: {ticket.status}")


def get_ticket_index(ticket_service, action):
    if not ticket_service.has_tickets():
        print("No tickets found.")
        return None

    try:
        ticket_number = int(input(f"Ticket number to {action}: "))
    except ValueError:
        print("Invalid ticket number. Please enter a number.")
        return None

    ticket_index = ticket_number - 1

    if not ticket_service.is_valid_ticket_index(ticket_index):
        print("Invalid ticket number.")
        return None

    return ticket_index


def list_tickets(ticket_service):
    tickets = ticket_service.list_tickets()

    if not tickets:
        print("No tickets found.")
        return

    for index, ticket in enumerate(tickets, start=1):
        display_ticket(ticket, index)


def search_tickets(ticket_service):
    if not ticket_service.has_tickets():
        print("No tickets found.")
        return

    search_term = input("Search term: ")
    found_tickets = ticket_service.search_tickets(search_term)

    if not found_tickets:
        print("No matching tickets found.")
        return

    for index, ticket in enumerate(found_tickets, start=1):
        display_ticket(ticket, index)


def close_ticket(ticket_service):
    ticket_index = get_ticket_index(ticket_service, "close")

    if ticket_index is None:
        return

    ticket_service.close_ticket(ticket_index)
    print("Ticket closed successfully.")


def delete_ticket(ticket_service):
    ticket_index = get_ticket_index(ticket_service, "delete")

    if ticket_index is None:
        return

    deleted_ticket = ticket_service.delete_ticket(ticket_index)
    print(f"Ticket deleted successfully: {deleted_ticket.title}")


def update_ticket(ticket_service):
    ticket_index = get_ticket_index(ticket_service, "update")

    if ticket_index is None:
        return

    selected_ticket = ticket_service.list_tickets()[ticket_index]

    print("Press Enter to keep the current value.")
    title = input(f"Title [{selected_ticket.title}]: ")
    description = input(f"Description [{selected_ticket.description}]: ")
    category = input(f"Category [{selected_ticket.category}]: ")
    priority = input(f"Priority [{selected_ticket.priority}]: ")
    status = input(f"Status [{selected_ticket.status}]: ")

    updated_ticket = ticket_service.update_ticket(
        ticket_index=ticket_index,
        title=title,
        description=description,
        category=category,
        priority=priority,
        status=status,
    )

    print("\nTicket updated successfully!")
    display_ticket(updated_ticket, ticket_index + 1)


def run_menu():
    ticket_service = TicketService()

    while True:
        print("\nAI Ticket Analyzer")

        for option_number, option_label in MENU_OPTIONS.items():
            print(f"{option_number}. {option_label}")

        choice = input("Choose an option: ")

        if choice not in MENU_OPTIONS:
            print("Invalid option. Please try again.")
            continue

        if choice == "1":
            create_ticket(ticket_service)
        elif choice == "2":
            list_tickets(ticket_service)
        elif choice == "3":
            search_tickets(ticket_service)
        elif choice == "4":
            update_ticket(ticket_service)
        elif choice == "5":
            close_ticket(ticket_service)
        elif choice == "6":
            delete_ticket(ticket_service)
        elif choice == "0":
            print("Goodbye!")
            break
