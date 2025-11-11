import datetime

class Project:
    def __init__(self, name='', start_date="", priority=0.0, cost=0.0, completion_percentage=0.0):
        self.name = name
        self.priority = priority
        self.cost = cost
        self.completion_percentage = completion_percentage
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()

    def __lt__(self, other):
        """Sort projects by priority (lower number = higher priority)."""
        return self.priority < other.priority

    def is_complete(self) -> bool:
        """Return True if project is complete."""
        return self.completion_percentage>= 100

    def display_str(self) -> str:
        """Return a formatted string representation of the project."""
        start_str = self.start_date.strftime(DATE_FORMAT)
        return f"{self.name}, start: {start_str}, priority: {self.priority}, estimate: ${self.cost:.2f}, completion: {self.percent_complete}%"