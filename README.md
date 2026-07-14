# AI Ticket Analyzer

AI Ticket Analyzer is a Python command-line project for working with support tickets.

The app can create, list, search, update, close, and delete tickets. It also stores tickets in a SQLite database, shows simple ticket statistics, exports charts, and includes a basic machine learning feature for predicting ticket categories.

## Technologies

- Python
- SQLite
- Pandas
- NumPy
- Matplotlib
- scikit-learn
- Git

## Main Features

- Create support tickets
- List all tickets
- Search tickets by title or description
- Update existing tickets
- Close tickets
- Delete tickets
- Save tickets in a SQLite database
- Show ticket statistics
- Export simple charts
- Predict ticket category from title and description

## Project Structure

```text
ai-ticket-analyzer/
|-- data/
|   `-- training_tickets.csv
|-- docs/
|-- src/
|   |-- analysis/
|   |-- machine_learning/
|   |-- database.py
|   |-- menu.py
|   |-- ticket.py
|   |-- ticket_repository.py
|   `-- ticket_service.py
|-- main.py
|-- requirements.txt
`-- README.md
```

## How To Run

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required packages:

```powershell
python -m pip install -r requirements.txt
```

Run the app:

```powershell
python main.py
```

## Menu Options

```text
1. Create ticket
2. List tickets
3. Search ticket
4. Update ticket
5. Close ticket
6. Delete ticket
7. Show ticket statistics
8. Export analysis charts
9. Train category classifier
10. Predict ticket category
0. Exit
```

## Notes

The SQLite database is created automatically when the app runs.

Ticket data is stored locally in:

```text
data/tickets.db
```

The file is ignored by Git because it is generated while using the app.

The machine learning example uses this CSV file:

```text
data/training_tickets.csv
```
