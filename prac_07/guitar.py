
CURRENT_YEAR = 2025
VINTAGE_AGE = 50

class Guitar:
    def __init__(self, name="", year=0, cost=0,):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return name, year and cost of guitar."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        """"Compare guitars by year."""
        return self.year < other.year


    def get_age(self):
        """Calculate age based on year it was made."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage or not based on age."""
        return self.get_age() >= VINTAGE_AGE