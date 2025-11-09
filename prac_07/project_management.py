from prac_07.project import Project
from datetime import date, datetime

DEFAULT_FILENAME = "projects.txt"

def main():
    print("Welcome to Pythonic Project Management")
    project, projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    menu_input = input("(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate project\n(Q)uit\n").upper()
    while menu_input != "Q":
        if menu_input == "L":
            project, projects = load_projects(projects)
        elif menu_input == "S":
            save_projects(projects)
        elif menu_input == "D":
            display_objects(projects)
        elif menu_input == "F":
            filter_projects(projects)
        elif menu_input == "A":
            add_projects(projects)
        elif menu_input == "U":
            update_projects(projects)
        else:
            print("Invalid menu choice")
            menu_input = input("(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate project\n(Q)uit\n").upper()

def add_projects(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost Estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost, completion_percentage)
    projects.append(new_project)

def load_projects(project):
    """Read data from file formatted like: Name, Start Date, Priority, Cost Estimate, Completion Percentage."""
    projects = []
    with open(DEFAULT_FILENAME, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
            print(project)
    return project, projects


def save_projects(DEFAULT_FILENAME, projects):
    """Save the projects list to the outfile, overwriting any existing content."""
    with open(DEFAULT_FILENAME, 'w') as outfile:
        for project in projects:
            outfile.write(project)

def filter_projects(projects):
    chosen_date = input("Show projects that start after date (dd/mm/yy): ")
    chosen_date = datetime.strptime(chosen_date, "%d/%m/%Y").date()
    for project in projects:
        if project.start_date > chosen_date:
            print(project)

def update_projects(projects):
    index = 0
    for project in projects:
        print(index, project)
        index += 1
    is_valid_input = False
    while not is_valid_input:
        choice = int(input("Project choice: "))
        if choice < 1:
            print("Number must be >=1")
        else:
            print(projects[choice])
            is_valid_input = True
        new_percentage = int(input("New Percentage: "))
        projects[choice].is_complete = new_percentage
    return projects




main()