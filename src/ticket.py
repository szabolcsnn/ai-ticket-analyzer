from dataclasses import dataclass


@dataclass
class Ticket:
    title: str
    description: str
    category: str
    priority: str
    status: str = "open"
    id: int | None = None
