import mysql.connector
from faker import Faker
import random
import string

fake = Faker()

# Database connection details (replace with your own credentials)
db_config = {
    'host': 'localhost',
    'port': 3308,
    'user': 'root',
    'password': '123456789',
    'database': 'school_management'
}

def generate_random_teacher():
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    gender = random.choice(['Male', 'Female'])
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    phone_number = fake.phone_number()

    return {
        'FirstName': first_name,
        'LastName': last_name,
        'EmailAddress': email,
        'Gender': gender,
        'Password': password,
        'PhoneNumber': phone_number
    }

def generate_random_teachers(num_teachers):
    teachers = []
    for _ in range(num_teachers):
        teacher = generate_random_teacher()
        teachers.append(teacher)
    return teachers

def connect_to_database():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print(f"Connected to MySQL database: {db_config['database']}")
            return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def close_database_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Connection closed.")

def insert_teacher_into_database(connection, teacher):
    cursor = connection.cursor()

    # SQL query to insert a teacher into the Teachers table
    insert_query = """
    INSERT INTO Teachers (FirstName, LastName, EmailAddress, Gender, Password, PhoneNumber)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    # Values to be inserted
    values = (
        teacher['FirstName'],
        teacher['LastName'],
        teacher['EmailAddress'],
        teacher['Gender'],
        teacher['Password'],
        teacher['PhoneNumber']
    )

    try:
        cursor.execute(insert_query, values)
        connection.commit()
        print(f"Teacher inserted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()
    finally:
        cursor.close()

if __name__ == "__main__":
    num_teachers = 20
    connection = connect_to_database()

    if connection:
        try:
            random_teachers = generate_random_teachers(num_teachers)

            for i, teacher in enumerate(random_teachers, 1):
                print(f"Inserting Teacher {i} into the database:")
                for key, value in teacher.items():
                    print(f"{key}: {value}")
                insert_teacher_into_database(connection, teacher)

        finally:
            close_database_connection(connection)
