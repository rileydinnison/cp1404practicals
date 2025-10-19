"""
Emails
Estimate: 50 minutes
Actual:   43 minutes
"""

def main():
    """Stores user's email and names in dictionary."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = find_name_in_email(email)
        confirmation = input(f"Is your name {name}? ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def find_name_in_email(email):
    """Find name in the email and extract it."""
    prefix = email.split('@')[0]
    names = prefix.split('.')
    name = " ".join(names).title()
    return name

main()