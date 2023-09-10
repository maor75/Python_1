import mysql.connector
from datetime import datetime

class DatabaseManager:
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

    def insert_or_update_user(self, user_id, first_name, last_name):
        select_query = "SELECT iduser FROM user WHERE iduser = %s"
        update_query = "UPDATE user SET last_name = %s, first_name = %s WHERE iduser = %s"
        insert_query = "INSERT INTO user (iduser, last_name, first_name) VALUES (%s, %s, %s)"

        self.cursor.execute(select_query, (user_id,))
        existing_record = self.cursor.fetchone()

        if existing_record:
            self.cursor.execute(update_query, (last_name, first_name, user_id))
        else:
            self.cursor.execute(insert_query, (user_id, last_name, first_name))

        self.connection.commit()

    def insert_sale(self, user_id, product_id):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        insert_query = "INSERT INTO sell (user_id, product_id, time) VALUES (%s, %s, %s)"

        self.cursor.execute(insert_query, (user_id, product_id, current_time))
        self.connection.commit()

    def insert_product(self, idproduct, product_name, descripsion):
        insert_query = "INSERT INTO product (idproduct, name_product, descripsion) VALUES (%s, %s, %s)"

        self.cursor.execute(insert_query, (idproduct, product_name, descripsion))
        self.connection.commit()



if __name__ == "__main__":

 # Example usage:
 db_manager = DatabaseManager()

 # Insert or update a user
 user_id = input("input the id: ")
 first_name = input("what is the first name: ")
 last_name = input("what is the last name: ")
 db_manager.insert_or_update_user(user_id, first_name, last_name)


 # Insert a product
 product_id = input("what is the product id?: ")
 product_name = input("what is thae product name?: ")
 description = input("input please a description: ")
 db_manager.insert_product(product_id, product_name, description)

  # Insert a sale
 user_id = input("what is the user id?: ")
 product_id = input("what is the product id?: ")
 db_manager.insert_sale(user_id, product_id)


 # Close the database connection
 db_manager.close_connection()
