users = {}  # Dictionary to store user information


def register_user():
    name = input("Enter your name: ")
    staff_id = input("Enter your staff ID: ")
    email = input("Enter your email address: ")
    password = input("Enter your preferred password: ")
    users[email] = {
        'name': name,
        'staff_id': staff_id,
        'password': password,
        'logged_in': False
    }
    print("Registration successful!")


def login_user():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    if email in users and users[email]['password'] == password:
        users[email]['logged_in'] = True
        print(f"Welcome, {users[email]['name']}!")
        perform_actions(email)
    else:
        print("Invalid email or password. Please try again.")


def perform_actions(email):
    while users[email]['logged_in']:
        print("\nActions:")
        print("1. Get point coordinates")
        print("2. Draw polygon")
        print("3. Draw line")
        print("4. Enable GIS layers")
        print("5. Enable Google Earth coordinates")
        print("6. Reset password")
        print("7. Log out")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            get_point_coordinates()
        elif choice == '2':
            draw_polygon()
        elif choice == '3':
            draw_line()
        elif choice == '4':
            enable_gis_layers()
        elif choice == '5':
            enable_google_earth_coordinates()
        elif choice == '6':
            reset_password(email)
        elif choice == '7':
            users[email]['logged_in'] = False
            print("Logged out successfully!")
        else:
            print("Invalid choice. Please try again.")


def get_point_coordinates():
    print("Getting point coordinates...")
    # Code to get point coordinates goes here


def draw_polygon():
    print("Drawing polygon...")
    # Code to draw a polygon goes here


def draw_line():
    print("Drawing line...")
    # Code to draw a line goes here


def enable_gis_layers():
    print("Enabling GIS layers...")
    # Code to enable GIS layers goes here


def enable_google_earth_coordinates():
    print("Enabling Google Earth coordinates...")
    # Code to enable Google Earth coordinates goes here


def reset_password(email):
    new_password = input("Enter a new password: ")
    users[email]['password'] = new_password
    print("Password reset successful!")


# Usage example
register_user()  # Register a new user
login_user()  # Log in as a registered user

