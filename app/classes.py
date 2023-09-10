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

class ProductDatabase:
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

    def search_product_by_id(self, product_id):
        try:
            query = "SELECT idproduct, name_product, descripsion FROM product WHERE idproduct = %s"
            self.cursor.execute(query, (product_id,))
            result = self.cursor.fetchone()

            if result:
                product_id, name_product, descripsion = result
                return product_id, name_product, descripsion
            else:
                return None
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def search_product_by_name(self, product_name):
        try:
            query = "SELECT idproduct, name_product, descripsion FROM product WHERE name_product = %s"
            self.cursor.execute(query, (product_name,))
            results = self.cursor.fetchall()

            if results:
                return results
            else:
                return None
        except mysql.connector.Error as err:
            print(f"Error: {err}")

class SellDatabase:

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

    def search_sells_by_time_range(self, start_time, end_time):
        try:
            query = """
            SELECT sell.user_id, sell.product_id, sell.time,
                   user.first_name, user.last_name,
                   product.name_product, product.descripsion
            FROM sell
            JOIN user ON sell.user_id = user.iduser
            JOIN product ON sell.product_id = product.idproduct
            WHERE sell.time BETWEEN %s AND %s
            """
            self.cursor.execute(query, (start_time, end_time))
            results = self.cursor.fetchall()

            if results:
                sell_data = []
                for row in results:
                    user_id, product_id, time, first_name, last_name, product_name, descripsion = row
                    sell_info = {
                        'User ID': user_id,
                        'Product ID': product_id,
                        'Time': time,
                        'First Name': first_name,
                        'Last Name': last_name,
                        'Product Name': product_name,
                        'Descripsion': descripsion
                    }
                    sell_data.append(sell_info)
                return sell_data
            else:
                return None
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def search_sells_by_product_id(self, product_id):
        try:
            query = """
            SELECT sell.user_id, sell.product_id, sell.time,
                   user.first_name, user.last_name,
                   product.name_product, product.descripsion
            FROM sell
            JOIN user ON sell.user_id = user.iduser
            JOIN product ON sell.product_id = product.idproduct
            WHERE sell.product_id = %s
            """
            self.cursor.execute(query, (product_id,))
            results = self.cursor.fetchall()

            if results:
                sell_data = []
                for row in results:
                    user_id, product_id, time, first_name, last_name, product_name, descripsion = row
                    sell_info = {
                        'User ID': user_id,
                        'Product ID': product_id,
                        'Time': time,
                        'First Name': first_name,
                        'Last Name': last_name,
                        'Product Name': product_name,
                        'Descripsion': descripsion
                    }
                    sell_data.append(sell_info)
                return sell_data
            else:
                return None
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def search_sells_by_user_id(self, user_id):

        try:
            query = """
            SELECT sell.product_id, sell.time,
                   user.first_name, user.last_name,
                   product.name_product, product.descripsion
            FROM sell
            JOIN user ON sell.user_id = user.iduser
            JOIN product ON sell.product_id = product.idproduct
            WHERE sell.user_id = %s
            """
            self.cursor.execute(query, (user_id,))
            results = self.cursor.fetchall()

            if results:
                sell_data = []
                for row in results:
                    product_id, time, first_name, last_name, product_name, descripsion = row
                    sell_info = {
                        'User ID': user_id,
                        'Product ID': product_id,
                        'Time': time,
                        'First Name': first_name,
                        'Last Name': last_name,
                        'Product Name': product_name,
                        'Descripsion': descripsion
                    }
                    sell_data.append(sell_info)
                return sell_data
            else:
                return None
        except mysql.connector.Error as err:
            print(f"Error: {err}")

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



