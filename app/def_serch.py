import mysql.connector

def get_name_and_last_name_by_id(id):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="change-me",
        database="project"  # Replace with your actual database name
    )
    cursor = connection.cursor()

    try:
        query = "SELECT first_name, last_name FROM user WHERE iduser = %s"  # Filter by the provided ID
        cursor.execute(query, (id,))
        result = cursor.fetchone()

        if result:
            first_name, last_name = result
            return first_name, last_name
        else:
            return None  # Return None if no matching record found
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

# Get input from the user
id = input("Enter the ID: ")

# Call the function with the provided ID
name_and_last_name = get_name_and_last_name_by_id(id)

if name_and_last_name:
    first_name, last_name = name_and_last_name
    print(f"The id is: {id}")
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
else:
    print("No matching record found for the provided ID.")


def get_name_and_last_name_by_id(id):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="change-me",
        database="project"  # Replace with your actual database name
    )
    cursor = connection.cursor()

    try:
        query = "SELECT first_name, last_name FROM user WHERE iduser = %s"  # Filter by the provided ID
        cursor.execute(query, (id,))
        result = cursor.fetchone()

        if result:
            first_name, last_name = result
            return first_name, last_name
        else:
            return None  # Return None if no matching record found
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()