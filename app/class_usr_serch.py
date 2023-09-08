import mysql.connector

class UserDatabase:
    def __init__(self, host="localhost", user="root", password="edmon", database="project"):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

    def get_by_id(self, user_id):
        try:
            query = "SELECT first_name, last_name FROM user WHERE iduser = %s"
            self.cursor.execute(query, (user_id,))
            result = self.cursor.fetchone()

            if result:
                first_name, last_name = result
                return first_name, last_name
            else:
                return None
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def get_by_name(self, first_name):
        try:
            query = "SELECT iduser, first_name, last_name FROM user WHERE first_name = %s"
            self.cursor.execute(query, (first_name,))
            results = self.cursor.fetchall()

            if results:
                return results
            else:
                return None
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def get_by_last_name(self, last_name):
        try:
            query = "SELECT iduser, first_name, last_name FROM user WHERE last_name = %s"
            self.cursor.execute(query, (last_name,))
            results = self.cursor.fetchall()

            if results:
                return results
            else:
                return None
        except mysql.connector.Error as err:
            print(f"Error: {err}")


if __name__ == "__main__":
 # Example usage:
 db = UserDatabase()

 # Get user by ID
 user_id = input("Enter the ID: ")
 name_and_last_name = db.get_by_id(user_id)

 if name_and_last_name:
    first_name, last_name = name_and_last_name
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
 else:
    print("No matching record found for the provided ID.")

 # Search by first name
 search_first_name = input("Enter the first name to search: ")
 results = db.get_by_name(search_first_name)

 if results:
    print("Matching users by first name:")
    for result in results:
        user_id, first_name, last_name = result
        print(f"ID: {user_id}, First Name: {first_name}, Last Name: {last_name}")
 else:
    print("No matching records found for the provided first name.")

 # Search by last name
 search_last_name = input("Enter the last name to search: ")
 results = db.get_by_last_name(search_last_name)

 if results:
    print("Matching users by last name:")
    for result in results:
        user_id, first_name, last_name = result
        print(f"ID: {user_id}, First Name: {first_name}, Last Name: {last_name}")
 else:
    print("No matching records found for the provided last name.")

 # Close the database connection
 db.close_connection()
