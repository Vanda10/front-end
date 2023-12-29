import mysql.connector
from faker import Faker
import random

# Create MySQL database connection
conn = mysql.connector.connect(
    host='localhost',
    port=3308,
    user='root',
    password='123456789',
    database='school_management'
)

cursor = conn.cursor()

# Create Students table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        FirstName VARCHAR(45),
        LastName VARCHAR(45),
        EmailAddress VARCHAR(45),
        Gender VARCHAR(45),
        Class VARCHAR(45),
        Password VARCHAR(45),
        PhoneNumber VARCHAR(45)
    )
''')

# Function to generate and insert random students
def generate_random_students(num_students):
    fake = Faker()

    for _ in range(num_students):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        gender = random.choice(['Male', 'Female'])
        student_class = random.choice(['M1', 'M2', 'M3'])
        password = fake.password()
        phone_number = fake.phone_number()

        # Insert the generated data into the Students table
        cursor.execute('''
            INSERT INTO Students (FirstName, LastName, EmailAddress, Gender, Class, Password, PhoneNumber)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''', (first_name, last_name, email, gender, student_class, password, phone_number))

# Generate and insert 60 random students with three classes of 20 students each
generate_random_students(60)

# Commit the changes and close the connection
conn.commit()
conn.close()
