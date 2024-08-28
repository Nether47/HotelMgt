import mysql.connector

def create_database_and_tables():
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin"  # Replace with your MySQL root password
    )
    cursor = connection.cursor()

    # Create the database
    cursor.execute("CREATE DATABASE IF NOT EXISTS hotel_sunset")
    cursor.execute("USE hotel_sunset")

    # Create the tables
    tables = {
        "employees": """
            CREATE TABLE IF NOT EXISTS employees (
                emp_id INT AUTO_INCREMENT PRIMARY KEY,
                emp_name VARCHAR(100) NOT NULL,
                gender ENUM('Male', 'Female', 'Other') NOT NULL,
                emp_age INT NOT NULL,
                shift ENUM('Morning', 'Evening', 'Night') NOT NULL,
                shift_hour INT NOT NULL,
                salary DECIMAL(10, 2) NOT NULL
            )
        """,
        "rooms": """
            CREATE TABLE IF NOT EXISTS rooms (
                room_no INT PRIMARY KEY,
                room_type VARCHAR(20) NOT NULL,
                prices DECIMAL(10, 2) NOT NULL,
                status ENUM('Available', 'Booked') DEFAULT 'Available'
            )
        """,
        "booking": """
            CREATE TABLE IF NOT EXISTS booking (
                booking_id INT PRIMARY KEY,
                room_type VARCHAR(20) NOT NULL,
                guest_name VARCHAR(255),
                phone_number VARCHAR(15) NOT NULL,
                room_number INT NOT NULL,
                check_in_date DATE,
                check_out_date DATE,
                total_days INT,
                price DECIMAL(10, 2),
                FOREIGN KEY (room_number) REFERENCES rooms(room_no)
            )
        """,
        "orders": """
            CREATE TABLE IF NOT EXISTS orders (
                order_id INT AUTO_INCREMENT PRIMARY KEY,
                dish_id INT,
                name VARCHAR(255) NOT NULL,
                quantity INT NOT NULL,
                item_price DECIMAL(10, 2) NOT NULL,
                total_price DECIMAL(10, 2) NOT NULL,
                mobile_no VARCHAR(15),
                address VARCHAR(255)
            )
        """,
        "menu": """
            CREATE TABLE IF NOT EXISTS menu (
                dish_id INT AUTO_INCREMENT PRIMARY KEY,
                dish_name VARCHAR(255) NOT NULL,
                description TEXT,
                price DECIMAL(10, 2) NOT NULL
            )
        """,
        "fdback": """
            CREATE TABLE IF NOT EXISTS fdback (
                name VARCHAR(255),
                feedback TEXT
            )
        """,
        "users": """
            CREATE TABLE IF NOT EXISTS users (
                user_id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(50) NOT NULL,
                role ENUM('admin', 'customer') DEFAULT 'customer'
            )
        """
    }

    # Execute table creation
    for table_name, table_query in tables.items():
        cursor.execute(table_query)
        print(f"Table '{table_name}' created successfully.")

    # Insert initial data
    initial_data = {
        "employees": """
            INSERT INTO employees (emp_name, gender, emp_age, shift, shift_hour, salary) VALUES
            ('John Doe', 'Male', 35, 'Morning', 8, 50000.00),
            ('Jane Smith', 'Female', 28, 'Evening', 6, 25000.00),
            ('Emily Johnson', 'Female', 40, 'Night', 10, 45000.00),
            ('Michael Brown', 'Male', 50, 'Morning', 8, 60000.00);
        """,
        "rooms": """
            INSERT INTO rooms (room_no, room_type, prices, status) VALUES
            (101, 'Deluxe', 15000.00, 'Available'),
            (102, 'Deluxe', 15000.00, 'Available'),
            (201, 'Double', 25000.00, 'Available'),
            (202, 'Double', 25000.00, 'Booked'),
            (301, 'King', 40000.00, 'Available'),
            (302, 'King', 40000.00, 'Booked'),
            (401, 'Balcony', 45000.00, 'Available'),
            (402, 'Balcony', 45000.00, 'Available'),
            (501, 'Cabana', 90000.00, 'Available');
        """,
        "menu": """
            INSERT INTO menu (dish_name, description, price) VALUES
    (1, 'Idli', 'Veg.', 150),
    (2, 'Vada', 'Veg.', 150),
    (3, 'Masala Dosa', 'Veg.', 200),
    (4, 'Plain Dosa', 'Veg.', 150),
    (5, 'Chole Bhature', 'Veg.', 160),
    (6, 'Upma', 'Veg.', 150),
    (7, 'Masala Upma', 'Veg.', 180),
    (8, 'Puri', 'Veg.', 140),
    (9, 'Halwa', 'Veg.', 150),
    (10, 'Aloo Chop', 'Veg.', 160),
    (11, 'Plain Rice', 'Veg.', 220),
    (12, 'Fried Rice', 'Veg.', 260),
    (13, 'Biryani', 'Veg.', 300),
    (14, 'Paneer Biryani', 'Veg.', 350),
    (15, 'Special Biryani', 'Non-Veg.', 450),
    (16, 'Chicken Biryani', 'Non-Veg.', 400),
    (17, 'Roti', 'Veg.', 100),
    (18, 'Tandoori Roti', 'Veg.', 130),
    (19, 'Plain Naan', 'Veg.', 100),
    (20, 'Masala Naan', 'Veg.', 120),
    (21, 'Butter Naan', 'Veg.', 130),
    (22, 'Paratha', 'Veg.', 100),
    (23, 'Lachha Paratha', 'Veg.', 140),
    (24, 'Methi Paratha', 'Veg.', 150),
    (25, 'Paneer Butter Masala', 'Veg.', 240),
    (26, 'Paneer Khadai', 'Veg.', 270),
    (27, 'Mushroom Chilli', 'Veg.', 260),
    (28, 'Mushroom Curry', 'Veg.', 250),
    (29, 'Chicken Butter Masala', 'Non-Veg.', 300),
    (30, 'Chicken Tikka Masala', 'Non-Veg.', 350),
    (31, 'Mutton Curry', 'Non-Veg.', 320),
    (32, 'Mix Veg Curry', 'Veg.', 280),
    (33, 'Iced Tea', 'Beverage', 180),
    (34, 'Masala Cold Drink', 'Beverage', 160),
    (35, 'Lemonade', 'Beverage', 140),
    (36, 'Soda Pop', 'Beverage', 150),
    (37, 'Butterscotch Icecream', 'Beverage', 190),
    (38, 'Vanilla Icecream', 'Beverage', 160),
    (39, 'Chocolate Icecream', 'Beverage', 180),
    (40, 'Water Bottle', 'Beverage', 100);
        """,
        "users": """
            INSERT INTO users (username, password, role) VALUES
            ('admin', 'admin123', 'admin'),
            ('customer1', 'cust123', 'customer');
        """
    }

    # Execute data insertion
    for table_name, insert_query in initial_data.items():
        cursor.execute(insert_query)
        print(f"Initial data inserted into '{table_name}' successfully.")

    # Commit changes and close the connection
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    create_database_and_tables()