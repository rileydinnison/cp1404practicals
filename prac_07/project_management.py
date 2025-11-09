from prac_07.project import Project

DEFAULT_FILENAME = "projects.txt"

def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects_from_file(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    menu_input = input("(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate project\n(Q)uit").upper()
    while menu_input != "Q":
        if menu_input == "L":
            load_projects()
        elif menu_input == "S":
            save_projects()
        elif menu_input == "D":
            display_objects
        elif menu_input == "F":
            filter_projects()
        elif menu_input == "A":
            add_projects()
        elif menu_input == "U":
            update_projects()
        else:
            print("Invalid menu choice")


def load_projects(filename=FILENAME):
    """Read data from file formatted like: Name, Start Date, Priority, Cost Estimate, Completion Percentage."""
    projects = []
    with open(filename, "r") as input_file:
        input_file.readline() # Skip first line
        for line in input_file:
            name, start_date, priority, cost, percent_complete = line.strip().split(',')
            project = Project(name, start_date, int(priority), float(cost), int(percent_complete))
            projects.append(project)
    return projects
