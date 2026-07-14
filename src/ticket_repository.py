from src.ticket import Ticket


class TicketRepository:
    def __init__(self, database_manager):
        self.database_manager = database_manager

    def create(self, ticket):
        with self.database_manager.get_connection() as connection:
            cursor = connection.execute(
                """
                INSERT INTO tickets (title, description, category, priority, status)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    ticket.title,
                    ticket.description,
                    ticket.category,
                    ticket.priority,
                    ticket.status,
                ),
            )
            ticket.id = cursor.lastrowid

        return ticket

    def get_all(self):
        with self.database_manager.get_connection() as connection:
            rows = connection.execute(
                """
                SELECT id, title, description, category, priority, status
                FROM tickets
                ORDER BY id
                """
            ).fetchall()

        return [self._row_to_ticket(row) for row in rows]

    def search(self, search_term):
        normalized_search_term = f"%{search_term.lower()}%"

        with self.database_manager.get_connection() as connection:
            rows = connection.execute(
                """
                SELECT id, title, description, category, priority, status
                FROM tickets
                WHERE lower(title) LIKE ? OR lower(description) LIKE ?
                ORDER BY id
                """,
                (normalized_search_term, normalized_search_term),
            ).fetchall()

        return [self._row_to_ticket(row) for row in rows]

    def update(self, ticket):
        with self.database_manager.get_connection() as connection:
            connection.execute(
                """
                UPDATE tickets
                SET title = ?, description = ?, category = ?, priority = ?, status = ?
                WHERE id = ?
                """,
                (
                    ticket.title,
                    ticket.description,
                    ticket.category,
                    ticket.priority,
                    ticket.status,
                    ticket.id,
                ),
            )

        return ticket

    def delete(self, ticket_id):
        with self.database_manager.get_connection() as connection:
            connection.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))

    def count(self):
        with self.database_manager.get_connection() as connection:
            row = connection.execute("SELECT COUNT(*) AS ticket_count FROM tickets").fetchone()

        return row["ticket_count"]

    def _row_to_ticket(self, row):
        return Ticket(
            id=row["id"],
            title=row["title"],
            description=row["description"],
            category=row["category"],
            priority=row["priority"],
            status=row["status"],
        )
