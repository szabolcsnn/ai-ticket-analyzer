import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(".cache") / "matplotlib"))

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt


class TicketAnalysis:
    def __init__(self, database_manager):
        self.database_manager = database_manager

    def load_tickets_dataframe(self):
        with self.database_manager.get_connection() as connection:
            return pd.read_sql_query(
                """
                SELECT id, title, description, category, priority, status
                FROM tickets
                ORDER BY id
                """,
                connection,
            )

    def get_statistics(self):
        tickets_dataframe = self.load_tickets_dataframe()

        if tickets_dataframe.empty:
            return {
                "total_tickets": 0,
                "by_status": {},
                "by_category": {},
                "by_priority": {},
                "status_percentages": {},
            }

        total_tickets = len(tickets_dataframe)
        status_counts = tickets_dataframe["status"].value_counts()

        return {
            "total_tickets": total_tickets,
            "by_status": status_counts.to_dict(),
            "by_category": tickets_dataframe["category"].value_counts().to_dict(),
            "by_priority": tickets_dataframe["priority"].value_counts().to_dict(),
            "status_percentages": np.round(
                (status_counts / total_tickets) * 100,
                2,
            ).to_dict(),
        }

    def save_summary_charts(self, output_directory=Path("docs") / "charts"):
        tickets_dataframe = self.load_tickets_dataframe()

        if tickets_dataframe.empty:
            return []

        output_directory = Path(output_directory)
        output_directory.mkdir(parents=True, exist_ok=True)

        chart_files = []
        chart_columns = {
            "status": "Tickets by Status",
            "category": "Tickets by Category",
            "priority": "Tickets by Priority",
        }

        for column, title in chart_columns.items():
            chart_file = output_directory / f"tickets_by_{column}.png"
            counts = tickets_dataframe[column].value_counts()

            figure, axis = plt.subplots(figsize=(8, 4))
            counts.plot(kind="bar", ax=axis, color="#4C78A8")
            axis.set_title(title)
            axis.set_xlabel(column.title())
            axis.set_ylabel("Ticket count")
            axis.tick_params(axis="x", rotation=30)
            figure.tight_layout()
            figure.savefig(chart_file)
            plt.close(figure)

            chart_files.append(chart_file)

        return chart_files
