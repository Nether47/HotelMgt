import mysql.connector
from tabulate import tabulate
import random

# Utility Functions
def get_connection():
    """Establish and return a new database connection."""
    return mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")

def execute_query(query, params=None):
    """Execute a database query and commit changes."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()

def fetch_data(query, params=None):
    """Fetch data from the database."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
            columns = [i[0] for i in cursor.description]
            return result, columns

def display_table(query, params=None):
    """Fetch data and display it in tabular format."""
    result, columns = fetch_data(query, params)
    print(tabulate(result, headers=columns, tablefmt="fancy_grid"))

# Admin Functions
def emp_details():
    display_table("SELECT * FROM employees")

def customdet():
    display_table("SELECT * FROM booking")

def room_details():
    while True:
        print("**********ROOM DETAILS**********")
        print("1. Show Rooms")
        print("2. Rooms Vacant")
        print("3. Rooms Booked")
        print("FOR EXIT ENTER ANY NO.: ")
        try:
            ch = int(input("Enter your choice: "))
            if ch == 1:
                display_table("SELECT room_type, prices, count(*) FROM rooms GROUP BY room_type, prices")
            elif ch == 2:
                display_table("SELECT * FROM rooms WHERE Status = %s", ("Available",))
            elif ch == 3:
                display_table("SELECT * FROM rooms WHERE Status = %s", ("Booked",))
            else:
                print("INVALID INPUT")
                break
        except ValueError:
            print("Please enter a valid number.")
            continue

def restaurant_details():
    display_table("SELECT * FROM orders")

def fedback():
    display_table("SELECT * FROM fdback")

# Booking Functions
def booking_id():
    """Generate a random booking ID."""
    return random.randint(10000, 99999)

def book_room(room_type, price_per_day):
    """Generalized function to book a room of any type."""
    try:
        room_number = random.randint(room_type['start'], room_type['end'])
        guest_name = input("Enter guest name: ")
        phone_number = input("Enter your phone number: ")
        check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
        check_out_date = input("Enter check-out date (YYYY-MM-DD): ")

        # Calculate total days
        total_days_query = "SELECT DATEDIFF(%s, %s)"
        days_result, _ = fetch_data(total_days_query, (check_out_date, check_in_date))
        total_days = days_result[0][0]

        # Calculate price
        total_price = price_per_day * total_days

        # Check room availability
        room_check_query = "SELECT * FROM rooms WHERE Status = 'Available' AND room_no = %s"
        room_result, _ = fetch_data(room_check_query, (room_number,))
        if not room_result:
            print("No available rooms.")
            return None

        # Update room status to 'booked'
        update_query = "UPDATE rooms SET Status = 'Booked' WHERE room_no = %s"
        execute_query(update_query, (room_number,))

        # Insert booking record
        booking_id = booking_id()
        insert_query = """
        INSERT INTO booking (Booking_ID, Room_Type, Guest_Name, Phone_number, Room_Number, Check_In_Date, Check_Out_Date, Total_Days, Price)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        execute_query(insert_query, (booking_id, room_type['name'], guest_name, phone_number, room_number, check_in_date, check_out_date, total_days, total_price))
        print(f"Room booked successfully! Room Number: {room_number}")

        # Display booking history
        display_table("SELECT * FROM booking WHERE Booking_ID = %s", (booking_id,))
        return booking_id
    except Exception as e:
        print(f"Error: {e}")

# Room Types
room_types = {
    1: {"name": "Deluxe", "price": 15000, "start": 101, "end": 111},
    2: {"name": "Double", "price": 25000, "start": 201, "end": 211},
    3: {"name": "King", "price": 40000, "start": 301, "end": 311},
    4: {"name": "Balcony", "price": 45000, "start": 401, "end": 411},
    5: {"name": "Cabana", "price": 90000, "start": 501, "end": 506}
}

def bookings():
    print("Choose Room Type to Book:")
    for key, room_type in room_types.items():
        print(f"{key}. {room_type['name']} Room")
    print("6. Exit")

    try:
        room_choice = int(input("Enter Your Option: "))
        if room_choice in room_types:
            book_room(room_types[room_choice], room_types[room_choice]['price'])
        elif room_choice == 6:
            print("Exiting...")
            return
        else:
            print("Invalid choice, please try again.")
    except ValueError:
        print("Please enter a valid number.")

# Gaming Section
def gaming():
    games = {
        1: ("Table Tennis", 15000),
        2: ("Bowling", 10000),
        3: ("Snooker", 25000),
        4: ("VR World Gaming", 40000),
        5: ("Video Games", 35000),
        6: ("Swimming Pool Games", 50000)
    }

    print("Available Games:")
    for key, (name, price) in games.items():
        print(f"{key}. {name} -----> {price} Rs./HR")
    print("7. Exit")

    try:
        game_choice = int(input("Enter What Game You Want To Play: "))
        if game_choice in games:
            hours = int(input("Enter No Of Hours You Want To Play: "))
            game_name, game_price = games[game_choice]
            total_price = hours * game_price
            print(f"YOU HAVE SELECTED TO PLAY: {game_name}")
            print(f"Total price = {total_price} Rs.")
        elif game_choice == 7:
            print("Exiting...")
        else:
            print("Invalid choice, please try again.")
    except ValueError:
        print("Please enter a valid number.")

# Feedback
def feedback():
    name = input("Enter your name: ")
    print("Write something about us...")
    feedback_text = input()
    insert_query = "INSERT INTO fdback (name, feedback) VALUES (%s, %s)"
    execute_query(insert_query, (name, feedback_text))
    print("\nTHANK YOU FOR YOUR FEEDBACK\nYOU HAVE BEEN REDIRECTED TO THE MAIN PAGE")

# Admin and Customer Slots
def admin_slot():
    while True:
        print("*********WELCOME ADMIN*********")
        print("1. Employees Details")
        print("2. Customer Details")
        print("3. Room Details")
        print("4. Feedback")
        print("5. Restaurant Details")
        print("6. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                emp_details()
            elif choice == 2:
                customdet()
            elif choice == 3:
                room_details()
            elif choice == 4:
                fedback()
            elif choice == 5:
                restaurant_details()
            elif choice == 6:
                break
            else:
                print("INVALID CHOICE, TRY AGAIN")
        except ValueError:
            print("Please enter a valid number.")

def customer_slot():
    """Function for customer interaction."""
    while True:
        print("*************NAMASTE*************")
        print("1. RESTAURANT")
        print("2. BOOK ROOMS")
        print("3. GAMING")
        print("4. FEEDBACK")
        print("5. EXIT")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                restaurant()
            elif choice == 2:
                bookings()
            elif choice == 3:
                gaming()
            elif choice == 4:
                feedback()
            elif choice == 5:
                break
            else:
                print("INVALID CHOICE, TRY AGAIN")
        except ValueError:
            print("Please enter a valid number.")

def admin_login():
    """Admin login function."""
    username = input("Enter Admin Username: ")
    password = input("Enter Admin Password: ")

    query = "SELECT * FROM users WHERE username = %s AND password = %s AND role = 'admin'"
    result, _ = fetch_data(query, (username, password))
    if result:
        print("Login successful. Welcome, Admin!")
        admin_slot()
    else:
        print("Invalid username or password. Please try again.")

def restaurant():
    """Function for restaurant menu and order management."""
    def menu():
        """Display the menu and handle order placement."""
        display_table("SELECT * FROM menu")
        try:
            yn = int(input("Do you want to order an item? Type (1 for yes/2 for back to main page): "))
            if yn == 1:
                place_order()
            elif yn == 2:
                print("THANK YOU, YOU HAVE BEEN REDIRECTED TO MAIN PAGE")
                customer_slot()
        except ValueError:
            print("Invalid input, redirecting to the main page.")
            customer_slot()

    def place_order():
        """Handle order placement by the customer."""
        try:
            dish_id = int(input("Enter Dish No.: "))
            quantity = int(input("Enter Quantity: "))
            name = input("Enter Your Name: ")
            mobile_no = input("Enter Mobile No.: ")
            address = input("Enter Address: ")

            # Fetch dish details
            query = "SELECT * FROM menu WHERE dish_id = %s"
            result, _ = fetch_data(query, (dish_id,))
            if not result:
                print("Invalid Dish ID.")
                return

            dish_name, item_price = result[0][1], result[0][3]
            total_price = item_price * quantity

            # Insert order details into orders table
            insert_query = """
            INSERT INTO orders (dish_id, name, quantity, item_price, total_price, mobile_no, address)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            execute_query(insert_query, (dish_id, dish_name, quantity, item_price, total_price, mobile_no, address))
            print("Order placed successfully! Redirecting to main page.")
        except ValueError:
            print("Invalid input. Please try again.")

    def view_orders():
        """View customer orders by mobile number."""
        try:
            mobile_no = input("Enter your mobile number: ")
            display_table("SELECT * FROM orders WHERE mobile_no = %s", (mobile_no,))
        except Exception as e:
            print(f"Error: {e}")

    def cancel_order():
        """Cancel customer orders."""
        try:
            mobile_no = input("Enter your mobile number to cancel orders: ")
            delete_query = "DELETE FROM orders WHERE mobile_no = %s"
            execute_query(delete_query, (mobile_no,))
            print("Your order has been cancelled. Redirecting to main page.")
        except Exception as e:
            print(f"Error: {e}")

    while True:
        print("\n1. VIEW MENU")
        print("2. VIEW YOUR ORDERS")
        print("3. CANCEL ORDER")
        print("4. FEEDBACK")
        print("5. EXIT")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                menu()
            elif choice == 2:
                view_orders()
            elif choice == 3:
                cancel_order()
            elif choice == 4:
                feedback()
            elif choice == 5:
                break
            else:
                print("INVALID CHOICE, TRY AGAIN")
        except ValueError:
            print("Please enter a valid number.")

def main_interface():
    """Main entry point for the hotel management system."""
    while True:
        print("*********WELCOME TO HOTEL SUNSET*********")
        print("1. Admin")
        print("2. Customer")
        print("3. Exit")
        try:
            user_type = int(input("Who are you? "))
            if user_type == 1:
                admin_login()
            elif user_type == 2:
                customer_slot()
            elif user_type == 3:
                print("Exiting... Thank you for visiting Hotel Sunset!")
                break
            else:
                print("INVALID CHOICE, PLEASE TRY AGAIN")
        except ValueError:
            print("Please enter a valid number.")

# Start the application
if __name__ == "__main__":
    main_interface()