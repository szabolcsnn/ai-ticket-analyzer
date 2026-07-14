# Architecture

AI Ticket Analyzer uses a simple layered architecture.

## Layers

```text
CLI layer
  menu.py

Business logic layer
  ticket_service.py

Data access layer
  ticket_repository.py
  database.py

Data model
  ticket.py

Analytics layer
  analysis/ticket_analysis.py

Machine learning layer
  machine_learning/ticket_classifier.py
```

## Request Flow

Creating a ticket:

```text
User input
  -> menu.py
  -> TicketService.create_ticket()
  -> TicketRepository.create()
  -> SQLite
```

Listing tickets:

```text
User input
  -> menu.py
  -> TicketService.list_tickets()
  -> TicketRepository.get_all()
  -> SQLite
```

Analytics:

```text
User input
  -> menu.py
  -> TicketAnalysis
  -> Pandas DataFrame
  -> statistics or chart files
```

Machine learning:

```text
training_tickets.csv
  -> TF-IDF vectorizer
  -> Multinomial Naive Bayes
  -> category prediction
```

## Design Decisions

- The CLI layer does not directly access SQLite.
- Ticket business logic is kept in `TicketService`.
- SQL queries are isolated in `TicketRepository`.
- Runtime data such as `tickets.db` and generated charts are ignored by Git.
- The ML classifier is intentionally simple and explainable.
