"""
Wimbledon
Estimate: 60 minutes
Actual:   84 minutes
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Process and display records of countries and champions."""
    records = read_file(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def process_records(records):
    """Create dictionary of champions and set of countries from records."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_to_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[INDEX_CHAMPION]] = 1
    return champion_to_count, countries

def read_file(FILENAME):
    """Read records from file"""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def display_results(champion_to_count, countries):
    """Display champions and countries"""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))

main()