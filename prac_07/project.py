class Project:
    """Represents a project with name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name: str, start_date: datetime, priority: int, cost: float, percent_complete: int):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.percent_complete = percent_complete

    def __lt__(self, other):
        """Sort projects by priority (lower number = higher priority)."""
        return self.priority < other.priority

    def is_complete(self) -> bool:
        """Return True if project is complete."""
        return self.percent_complete >= 100

    def display_str(self) -> str:
        """Return a formatted string representation of the project."""
        start_str = self.start_date.strftime(DATE_FORMAT)
        return f"{self.name}, start: {start_str}, priority: {self.priority}, estimate: ${self.cost:.2f}, completion: {self.percent_complete}%"