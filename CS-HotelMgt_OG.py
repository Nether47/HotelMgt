import mysql.connector
from tabulate import tabulate
import random

a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
y = a.cursor()

# All details for admin

# To show employee details
def emp_details():
    a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
    y = a.cursor()
    q = "select * from employees"
    y.execute(q)
    r = y.fetchall()
    columns = [i[0] for i in y.description]
    print(tabulate(r, headers=columns, tablefmt="fancy_grid"))

# To show customer details
def customdet():
    a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
    y = a.cursor()
    x = "select * from booking"
    y.execute(x)
    r = y.fetchall()
    columns = [i[0] for i in y.description]
    print(tabulate(r, headers=columns, tablefmt="fancy_grid"))
    a.commit()

# To show room details (all rooms, vacant rooms, booked rooms)
def room_details():
    while True:
        print("**********ROOM DETAILS**********")
        print("1. Show Rooms")
        print("2. Rooms Vacant")
        print("3. Rooms Booked")
        print("FOR EXIT ENTER ANY NO.: ")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            show_rooms()
        elif ch == 2:
            room_vacant()
        elif ch == 3:
            rooms_booked()
        else:
            print("INVALID INPUT")
            break

# To show all rooms
def show_rooms():
    a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
    y = a.cursor()
    y.execute("select room_type, prices, count(*) from rooms group by room_type, prices;")
    r = y.fetchall()
    columns = [i[0] for i in y.description]
    print(tabulate(r, headers=columns, tablefmt="fancy_grid"))

# To show room vacant
def room_vacant():
    a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
    y = a.cursor()
    av = "Available"
    z = "select * from rooms where Status ='{}'".format(av)
    y.execute(z)
    r = y.fetchall()
    columns = [i[0] for i in y.description]
    print(tabulate(r, headers=columns, tablefmt="fancy_grid"))

# To show booked rooms
def rooms_booked():
    a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
    y = a.cursor()
    bk = "Booked"
    x = "select * from rooms where Status ='{}'".format(bk)
    y.execute(x)
    r = y.fetchall()
    columns = [i[0] for i in y.description]
    print(tabulate(r, headers=columns, tablefmt="fancy_grid"))

# To show restaurant details
def restaurant_details():
    a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
    y = a.cursor()
    z = "select*from orders"
    y.execute(z)
    r = y.fetchall()
    columns = [i[0] for i in y.description]
    print(tabulate(r, headers=columns, tablefmt="fancy_grid"))

# To show all feedback
def fedback():
    a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
    y = a.cursor()
    x = "select * from fdback"
    y.execute(x)
    x = y.fetchall()
    columns = [i[0] for iin y.description]
    print(tabulate(r, headers=columns, tablefmt="fancy_grid"))

# To show customer details
def customdet():
    a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
    y = a.cursor()
    x = "select * from booking"
    y.execute(x)
    r = y.fetchall()
    columns = [i[0] for i in y.description]
    print(tabulate(r, headers=columns, tablefmt="fancy_grid"))
    a.commit()

# To show room details (all rooms, vacant rooms, booked rooms)
def room_details():
    while True:
        print("**********ROOM DETAILS**********")
        print("1. Show Rooms")
        print("2. Rooms Vacant")
        print("3. Rooms Booked")
        print("FOR EXIT ENTER ANY NO.: ")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            show_rooms()
        elif ch == 2:
            room_vacant()
        elif ch == 3:
            rooms_booked()
        else:
            print("INVALID INPUT")
            break

# To show all rooms
def show_rooms():
    a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
    y = a.cursor()
    y.execute("select room_type, prices, count(*) from rooms group by room_type, prices;")
    r = y.fetchall()
    columns = [i[0] for i in y.description]
    print(tabulate(r, headers=columns, tablefmt="fancy_grid"))

# To show room vacant
def room_vacant():
    a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
    y = a.cursor()
    av = "Available"
    z = "select * from rooms where Status ='{}'".format(av)
    y.execute(z)
    r = y.fetchall()
    columns = [i[0] for i in y.description]
    print(tabulate(r, headers=columns, tablefmt="fancy_grid"))

# To show booked rooms
def rooms_booked():
    a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
    y = a.cursor()
    bk = "Booked"
    x = "select * from rooms where Status ='{}'".format(bk)
    y.execute(x)
    r = y.fetchall()
    columns = [i[0] for i in y.description]
    print(tabulate(r, headers=columns, tablefmt="fancy_grid"))

# To show restaurant details
def restaurant_details():
    a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
    y = a.cursor()
    z = "select * from orders"
    y.execute(z)
    r = y.fetchall()
    columns = [i[0] for i in y.description]
    print(tabulate(r, headers=columns, tablefmt="fancy_grid"))

# To show all feedback
def fedback():
    a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
    y = a.cursor()
    x = "select * from fdback"
    y.execute(x)
    x = y.fetchall()
    columns = [i[0] for i in y.description]
    print(tabulate(x, headers=columns, tablefmt="fancy_grid"))

# Restaurant
def restaurant():
    # VIEW MENU
    def menu():
        a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
        y = a.cursor()
        b = "select * from menu".format()
        y.execute(b)
        menu = y.fetchall()
        columns = [i[0] for i in y.description]
        print(tabulate(menu, headers=columns, tablefmt="fancy_grid"))
        if len(menu) > 0:
            print("Available")
        a.commit()

        yn = int(input("Do you want to order an item? Type (1 for yes/2 for back to main page):"))
        if yn == 1:
            b_order()
        elif yn == 2:
            print("THANK YOU")
            print("YOU HAVE BEEN REDIRECTED TO MAIN PAGE")
            customer_slot()

    # BOOKING ORDER
    def b_order():
        a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
        y = a.cursor()
        Id = int(input("ENTER DISH NO.: "))
        Quantity = int(input("ENTER QUANTITY: "))
        Name = input("ENTER YOUR NAME: ")
        Mobile_No = int(input("Enter mobile no.: "))
        Address = input("Enter Address:")
        f = ("select * from menu where Dish_ID={}").format(Id)
        y.execute(f)
        x = y.fetchall()
        itn = x[0][1]
        ip = x[0][3]
        tp = ip * Quantity

        ins = "insert into orders(ID, Name, Quantity, Item_Price, Total_Price, Mobile_No, Adress) values({}, '{}', {}, {}, {}, {}, '{}')".format(Id, itn, Quantity, ip, tp, Mobile_No, Address)
        y.execute(ins)
        print("THANKS FOR THE ORDER", "\n\n", "YOUR ORDER HAS BEEN ORDERED SUCCESSFULLY", "\n\n")
        print("YOU HAVE BEEN REDIRECTED TO THE MAIN PAGE")
        a.commit()

    # VIEW ORDER
    def vorders():
        a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
        y = a.cursor()
        m = int(input("Enter your number :"))
        n = "select * from orders where Mobile_No={} ".format(m)
        print("\n", "YOUR RECENT ORDERS", "\n")
        y.execute(n)
        o = y.fetchall()
        columns = [i[0] for i in y.description]
        print(tabulate(o, headers=columns, tablefmt="fancy_grid"))
        for i in o:
            p = "select * from menu, orders where Mobile_No={} and menu.Dish_ID=orders.ID".format(m)
            y.execute(p)
            q = y.fetchall()
            a.commit()

    # CANCEL ORDER
    def corder():
        a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
        y = a.cursor()
        x = int(input("enter your number:"))
        s = "delete from orders where Mobile_No={}".format(x)
        y.execute(s)
        print("\n\n", "YOUR ORDER HAS BEEN CANCELLED")
        print("YOU HAVE BEEN REDIRECTED TO THE MAIN PAGE", "\n\n")
        a.commit()

    # FEEDBACK
    def fdback():
        a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
        y = a.cursor()
        fdn = input("Enter your name:")
        print("Write something about us...")
        fdi = input()
        x = "insert into fdback values('{}','{}')".format(fdn, fdi)
        y.execute(x)
        print("\n\n")
        print("THANK YOU FOR YOUR FEEDBACK")
        print("\n")
        print("YOU HAVE BEEN REDIRECTED TO THE MAIN PAGE")
        a.commit()

    # Welcome
    def start1():
        while True:
            print("\n")
            print("1. VIEW MENU")
            print("2. VIEW YOUR ORDERS")
            print("3. CANCEL ORDER")
            print("4. FEEDBACK")
            print("5. EXIT")
            ch1 = int(input("enter your choice:"))
            if ch1 == 1:
                menu()
            elif ch1 == 2:
                vorders()
            elif ch1 == 3:
                corder()
            elif ch1 == 4:
                fdback()
            elif ch1 == 5:
                break
            else:
                print("\n", "INVALID CHOICE", " \n", "TRY AGAIN.", " \n")

    start1()

# Booking rooms section
# Create the table if not exists
create_table = "CREATE TABLE IF NOT EXISTS booking (Booking_ID int(10) PRIMARY KEY, Room_Type varchar(20) not null, Guest_Name VARCHAR(255), Phone_number varchar(15) not null, Room_Number int(5) not null, Check_In_Date DATE, Check_Out_Date DATE)"
y.execute(create_table)

def booking_id():
    return random.randint(10000, 99999)

# To book room
def book_room(guest_name, ph_no, ro_no, check_in_date, check_out_date, td1, pr):
    try:
        a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
        y = a.cursor()
        b_id = booking_id()
        # Fetch available rooms
        c = "SELECT * FROM rooms WHERE Status = 'Available' and room_no={}".format(ro_no)
        y.execute(c)
        d = y.fetchall()
        if not d:
            print("No available rooms.")
            return None
        e = d[0]
        # Update room status to 'booked'
        update_query = "UPDATE rooms SET Status = 'Booked' WHERE room_no = {}".format(ro_no)
        y.execute(update_query)

        # Insert booking record
        ins = "INSERT INTO booking (Booking_ID, Room_Type, Guest_Name, Phone_number, Room_Number, Check_In_Date, Check_Out_Date, Total_Days, Price) VALUES ({}, '{}', '{}', {}, {}, '{}', '{}', {}, '{}')".format(
            b_id, e[1], guest_name, ph_no, ro_no, check_in_date, check_out_date, td1, pr)
        y.execute(ins)
        print("Room booked successfully! Room Number: ", ro_no)
        return b_id
    except:
        print("Error")
    finally:
        a.commit()

# To book deluxe room
def book_delux_room():
    a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
    y = a.cursor()
    try:
        z = random.randint(101, 111)
        ro_no = z
        g_name = input("Enter guest name: ")
        ph_no = input("Enter your phone number: ")
        in_date = input("Enter check-in date (YYYY-MM-DD): ")
        out_date = input("Enter check-out date (YYYY-MM-DD):")
        total_days_query = "SELECT DATEDIFF('{}', '{}')".format(out_date, in_date)
        y.execute(total_days_query)
        td1 = y.fetchone()[0]
        pr = 15000 * td1
        booking_id = book_room(g_name, ph_no, ro_no, in_date, out_date, td1, pr)
        # Display booking history for the specific Booking_ID
        if booking_id is not None:
            q = "SELECT * FROM booking WHERE Booking_ID = {}".format(booking_id)
            y.execute(q)
            print("\nBooking History for Booking_ID {}: ".format(booking_id))
            x = y.fetchall()
            columns = [i[0] for i in y.description]
            print(tabulate(x, headers=columns, tablefmt="fancy_grid"))
    except:
        print("Error")

# To book double room
def book_double_room():
    a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
    y = a.cursor()
    try:
        z = random.randint(201, 211)
        ro_no = z
        g_name = input("Enter guest name: ")
        ph_no = input("Enter your phone number: ")
        in_date = input("Enter check-in date (YYYY-MM-DD): ")
        out_date = input("Enter check-out date (YYYY-MM-DD):")
        total_days_query = "SELECT DATEDIFF('{}', '{}')".format(out_date, in_date)
        y.execute(total_days_query)
        td1 = y.fetchone()[0]
        pr = 25000 * td1
        booking_id = book_room(g_name, ph_no, ro_no, in_date, out_date, td1, pr)
        # Display booking history for the specific Booking_ID
        if booking_id is not None:
            q = "SELECT * FROM booking WHERE Booking_ID = {}".format(booking_id)
            y.execute(q)
            print("\nBooking History for Booking_ID {}: ".format(booking_id))
            x = y.fetchall()
            columns = [i[0] for i in y.description]
            print(tabulate(x, headers=columns, tablefmt="fancy_grid"))
    except:
        print("Error")

# To book king room
def book_king_room():
    a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
    y = a.cursor()
    try:
        z = random.randint(301, 311)
        ro_no = z
        g_name = input("Enter guest name: ")
        ph_no = input("Enter your phone number: ")
        in_date = input("Enter check-in date (YYYY-MM-DD): ")
        out_date = input("Enter check-out date (YYYY-MM-DD):")
        total_days_query = "SELECT DATEDIFF('{}', '{}')".format(out_date, in_date)
        y.execute(total_days_query)
        td1 = y.fetchone()[0]
        pr = 40000 * td1
        booking_id = book_room(g_name, ph_no, ro_no, in_date, out_date, td1, pr)
        # Display booking history for the specific Booking_ID
        if booking_id is not None:
            q = "SELECT * FROM booking WHERE Booking_ID = {}".format(booking_id)
            y.execute(q)
            print("\nBooking History for Booking_ID {}: ".format(booking_id))
            x = y.fetchall()
            columns = [i[0] for i in y.description]
            print(tabulate(x, headers=columns, tablefmt="fancy_grid"))
    except:
        print("Error")

# To book balcony room
def book_balcony_room():
    a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
    y = a.cursor()
    try:
        z = random.randint(401, 411)
        ro_no = z
        g_name = input("Enter guest name: ")
        ph_no = input("Enter your phone number: ")
        in_date = input("Enter check-in date (YYYY-MM-DD): ")
        out_date = input("Enter check-out date (YYYY-MM-DD):")
        total_days_query = "SELECT DATEDIFF('{}', '{}')".format(out_date, in_date)
        y.execute(total_days_query)
        td1 = y.fetchone()[0]
        pr = 45000 * td1
        booking_id = book_room(g_name, ph_no, ro_no, in_date, out_date, td1, pr)
        # Display booking history for the specific Booking_ID
        if booking_id is not None:
            q = "SELECT * FROM booking WHERE Booking_ID = {}".format(booking_id)
            y.execute(q)
            print("\nBooking History for Booking_ID {}: ".format(booking_id))
            x = y.fetchall()
            columns = [i[0] for i in y.description]
            print(tabulate(x, headers=columns, tablefmt="fancy_grid"))
    except:
        print("Error")

# To book cabana room
def book_cavana():
    a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
    y = a.cursor()
    try:
        z = random.randint(501, 506)
        ro_no = z
        g_name = input("Enter guest name: ")
        ph_no = input("Enter your phone number: ")
        in_date = input("Enter check-in date (YYYY-MM-DD): ")
        out_date = input("Enter check-out date (YYYY-MM-DD):")
        total_days_query = "SELECT DATEDIFF('{}', '{}')".format(out_date, in_date)
        y.execute(total_days_query)
        td1 = y.fetchone()[0]
        pr = 90000 * td1
        booking_id = book_room(g_name, ph_no, ro_no, in_date, out_date, td1, pr)
        # Display booking history for the specific Booking_ID
        if booking_id is not None:
            q = "SELECT * FROM booking WHERE Booking_ID = {}".format(booking_id)
            y.execute(q)
            print("\nBooking History for Booking_ID {}: ".format(booking_id))
            x = y.fetchall()
            columns = [i[0] for i in y.description]
            print(tabulate(x, headers=columns, tablefmt="fancy_grid"))
    except:
        print("Error")

# User choice
def bookings():
    try:
        a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
        y = a.cursor()
        z = "select * from book_rooms"
        y.execute(z)
        x = y.fetchall()
        columns = [i[0] for i in y.description]
        print(tabulate(x, headers=columns, tablefmt="fancy_grid"))
        roomchoice = int(input("Enter Your Option : "))
        if roomchoice == 1:
            book_delux_room()
        elif roomchoice == 2:
            book_double_room()
        elif roomchoice == 3:
            book_king_room()
        elif roomchoice == 4:
            book_balcony_room()
        elif roomchoice == 5:
            book_cavana()
        else:
            print("Sorry, May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
    except:
        print("Error")
    finally:
        y.close()
        a.close()

# Gaming section
def gaming():
    print("1. Table Tennis -----> 15000 Rs./HR")
    print("2. Bowling -----> 10000 Rs./HR")
    print("3. Snooker -----> 25000 Rs./HR")
    print("4. VR World Gaming -----> 40000 Rs./HR")
    print("5. Video Games -----> 35000 Rs./HR")
    print("6. Swimming Pool Games -----> 50000 Rs./HR")
    print("7. Exit")
    game = int(input("Enter What Game You Want To Play : "))
    hour = int(input("Enter No Of Hours You Want To Play : "))
    if game == 1:
        print("YOU HAVE SELECTED TO PLAY : Table Tennis")
        gamingbill = hour * 15000
        price = print("Total price = ", gamingbill, "Rs.")
    elif game == 2:
        print("YOU HAVE SELECTED TO PLAY : Bowling")
        gamingbill = hour * 10000
        price = print("Total price = ", gamingbill, "Rs.")
    elif game == 3:
        print("YOU HAVE SELECTED TO PLAY : Snooker")
        gamingbill =hour * 25000
        price = print("Total price = ", gamingbill, "Rs.")
    elif game == 4:
        print("YOU HAVE SELECTED TO PLAY : VR World Gaming")
        gamingbill = hour * 40000
        price = print("Total price = ", gamingbill, "Rs.")
    elif game == 5:
        print("YOU HAVE SELECTED TO PLAY : Video Games")
        gamingbill = hour * 35000
        price = print("Total price = ", gamingbill, "Rs.")
    elif game == 6:
        print("YOU HAVE SELECTED TO PLAY : Swimming Pool Games")
        gamingbill = hour * 50000
        price = print("Total price = ", gamingbill, "Rs.")
    else:
        print("Sorry, May Be You Are Giving Me Wrong Input, Please Try Again !!!")

# Feedback to be asked by user
def feedback():
    a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
    y = a.cursor()
    fdn = input("Enter your name:")
    print("Write something about us...")
    fdi = input()
    x = "insert into fdback values('{}','{}')".format(fdn, fdi)
    y.execute(x)
    print("\n\n")
    print("THANK YOU FOR YOUR FEEDBACK")
    print("\n")
    print("YOU HAVE BEEN REDIRECTED TO THE MAIN PAGE")
    a.commit()

# For admin
def admin_slot():
    while True:
        print("*********WELCOME ADMIN*********")
        print("1. Employees Details")
        print("2. Customer Details")
        print("3. Room Details")
        print("4. Feedback")
        print("5. Restaurant Details")
        print("6. Exit")
        a = int(input("Enter your choice: "))
        if a == 1:
            emp_details()
        elif a == 2:
            customdet()
        elif a == 3:
            room_details()
        elif a == 4:
            fedback()
        elif a == 5:
            restaurant_details()
        elif a == 6:
            break
        else:
            print("\n\n", "INVALID CHOICE", "\n", "TRY AGAIN")

# For customer
def customer_slot():
    while True:
        print("*************NAMASTE*************")
        print("1. RESTAURANT")
        print("2. BOOK ROOMS")
        print("3. GAMING")
        print("4. FEEDBACK")
        print("5. EXIT")
        a = int(input("Enter your choice: "))
        if a == 1:
            restaurant()
        elif a == 2:
            bookings()
        elif a == 3:
            gaming()
        elif a == 4:
            feedback()
        elif a == 5:
            break
        else:
            print("\n\n", "INVALID CHOICE")

# First interface
while True:
    print("*********WELCOME TO HOTEL SUNSET*********")
    print("1. Admin")
    print("2. Customer")
    print("3. Exit")
    a = int(input("Who are you? "))
    if a == 1:
        def admin_login(a, username, password):
            a = mysql.connector.connect(host="localhost", user="root", password="admin", database="hotel_sunset")
            y = a.cursor()
            try:
                # Check if the provided username and password match an admin record
                query = "SELECT * FROM users WHERE username = %s AND password = %s"
                y.execute(query, (username, password))
                admin_result = y.fetchone()
                if admin_result:
                    print("Login successful. Welcome, Admin!")
                else:
                    print("Invalid username or password. Please try again.")
            except Exception as e:
                print(f"Error: {e}")
            a.close()

        admin_username = input("Enter Admin Username: ")
        admin_password = input("Enter Admin Password: ")
        admin_login(a, admin_username, admin_password)
        admin_slot()
    elif a == 2:
        customer_slot()
    elif a == 3:
        break  