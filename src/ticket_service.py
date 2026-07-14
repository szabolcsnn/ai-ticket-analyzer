from src.ticket import Ticket


class TicketService:
    def __init__(self, ticket_repository):
        self.ticket_repository = ticket_repository

    def create_ticket(self, title, description, category, priority):
        ticket = Ticket(
            title=title,
            description=description,
            category=category,
            priority=priority,
        )
        return self.ticket_repository.create(ticket)

    def list_tickets(self):
        return self.ticket_repository.get_all()

    def search_tickets(self, search_term):
        return self.ticket_repository.search(search_term)

    def close_ticket(self, ticket_index):
        selected_ticket = self.list_tickets()[ticket_index]
        selected_ticket.status = "closed"
        return self.ticket_repository.update(selected_ticket)

    def delete_ticket(self, ticket_index):
        selected_ticket = self.list_tickets()[ticket_index]
        self.ticket_repository.delete(selected_ticket.id)
        return selected_ticket

    def update_ticket(
        self,
        ticket_index,
        title=None,
        description=None,
        category=None,
        priority=None,
        status=None,
    ):
        selected_ticket = self.list_tickets()[ticket_index]

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

        return self.ticket_repository.update(selected_ticket)

    def has_tickets(self):
        return self.ticket_repository.count() > 0

    def ticket_count(self):
        return self.ticket_repository.count()

    def is_valid_ticket_index(self, ticket_index):
        return 0 <= ticket_index < self.ticket_count()
