

def main():
    """Menu program that gets a valid score, prints result based on score and prints asterisks based on score"""
    score = get_valid_score()
    choice = input("Menu:\n(G)et a valid final_score\n(P)rint result\n(S)how stars\n(Q)uit\n").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        choice = input("Menu:\n(G)et a valid final_score\n(P)rint result\n(S)how stars\n(Q)uit\n").upper()
    print("Farewell")

def print_stars(score):
    """Print x amount of stars based on the user input for score"""
    for i in range(score):
        print("*", end= "")
    print()

def print_result(score):
    """Determine result based on score"""
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    print(result)


def get_valid_score():
    """Get valid score from user"""
    valid_score = int(input("Enter score: "))
    while valid_score < 0 or valid_score > 100:
        print("Invalid score")
        valid_score = int(input("Enter score: "))
    return valid_score

main()