import mysql.connector
from faker import Faker

# Create MySQL database connection
conn = mysql.connector.connect(
    host='localhost',
    port=3308,
    user='root',
    password='123456789',
    database='school_management'
)

cursor = conn.cursor()

# Create Courses table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Courses (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        CourseID VARCHAR(45),
        CourseName VARCHAR(45)
    )
''')

# Function to generate and insert random courses
def generate_random_courses(num_courses):
    fake = Faker()

    for _ in range(num_courses):
        abbreviation = fake.lexify(text='???')
        course_id_digit = fake.random_digit()
        course_id = f'{abbreviation}{course_id_digit}'
        course_name = fake.word()

        # Insert the generated data into the Courses table
        cursor.execute('''
            INSERT INTO Courses (CourseID, CourseName)
            VALUES (%s, %s)
        ''', (course_id, course_name))

# Generate and insert 20 random courses
generate_random_courses(20)

# Commit the changes and close the connection
conn.commit()
conn.close()
