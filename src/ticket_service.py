from src.ticket import Ticket


class TicketService:
    def __init__(self):
        self._tickets = []

    def create_ticket(self, title, description, category, priority):
        ticket = Ticket(
            title=title,
            description=description,
            category=category,
            priority=priority,
        )
        self._tickets.append(ticket)
        return ticket

    def list_tickets(self):
        return self._tickets.copy()

    def search_tickets(self, search_term):
        normalized_search_term = search_term.lower()
        found_tickets = []

        for ticket in self._tickets:
            title = ticket.title.lower()
            description = ticket.description.lower()

            if normalized_search_term in title or normalized_search_term in description:
                found_tickets.append(ticket)

        return found_tickets

    def close_ticket(self, ticket_index):
        selected_ticket = self._tickets[ticket_index]
        selected_ticket.status = "closed"
        return selected_ticket

    def delete_ticket(self, ticket_index):
        return self._tickets.pop(ticket_index)

    def update_ticket(
        self,
        ticket_index,
        title=None,
        description=None,
        category=None,
        priority=None,
        status=None,
    ):
        selected_ticket = self._tickets[ticket_index]

        if title:
            selected_ticket.title = title
        if description:
            selected_ticket.description = description
        if category:
            selected_ticket.category = category
        if priority:
            selected_ticket.priority = priority
        if status:
            selected_ticket.status = status

        return selected_ticket

    def has_tickets(self):
        return bool(self._tickets)

    def ticket_count(self):
        return len(self._tickets)

    def is_valid_ticket_index(self, ticket_index):
        return 0 <= ticket_index < len(self._tickets)
