import json


def filter_users_by_name(users: list, name: str) -> None:
    """
    Filter users by name given by user.
    :param users: list containing all users' data.
    :param name: str containing name provided by user.
    :return: None
    """
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_by_age(users: list, age: int) -> None:
    """
    Filter users by age given by user.
    :param users: list containing all users' data.
    :param age: int containing age provided by user.
    :return: None
    """
    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)


def filter_by_email(users: list, email: str) -> None:
    """
    Filter users by email given by user.
    :param users: list containing all users' data.
    :param email: str containing email provided by user.
    :return: None
    """
    filtered_users = [user for user in users if user["email"] == email]

    for user in filtered_users:
        print(user)


def dispatch_filter_by_name(users) -> None:
    """
    Get email to filter by from the user and dispatch to according function.
    :param users: list containing all users' data.
    :return: None
    """
    name_to_search = input("Enter a name to filter users: ").strip()
    filter_users_by_name(users, name_to_search)


def dispatch_filter_by_age(users) -> None:
    """
    Get age to filter by from the user and dispatch to according function.
    :param users: list containing all users' data.
    :return: None
    """
    age_to_search = int(input("Enter an age to filter users: ").strip())
    filter_by_age(users, age_to_search)


def dispatch_filter_by_email(users: list) -> None:
    """
    Get name to filter by from user and dispatch to according function.
    :param users: list containing all users' data.
    :return: None
    """
    email_to_search = input("Enter an email to filter users: ").strip()
    filter_by_email(users, email_to_search)


def dispatch_menu(users: list, user_input: str) -> None:
    """
    Display and dispatch the different commands from the menu.
    :param users: list containing all users' data.
    :param user_input: str provided by the user that should match a menu command.
    :return: None
    """
    menu = {
        "name": dispatch_filter_by_name,
        "age": dispatch_filter_by_age,
        "email": dispatch_filter_by_email,
        "exit": lambda _: (print("\nGoodbye!"), exit())[1]
    }

    if user_input in menu:
        menu[user_input](users)
    else:
        print("Filtering by that option is not yet supported.")


def load_data() -> list:
    """
    Load the users data from the users.json file.
    :return: users: list containing all users' data.
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    return users


def main():
    users = load_data()

    while True:
        filter_option = input("\nWhat would you like to filter by (or exit program)? (name/age/email/exit): ").strip().lower()
        dispatch_menu(users, filter_option)


if __name__ == "__main__":
    main()
