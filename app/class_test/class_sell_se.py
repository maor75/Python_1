import mysql.connector

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
    
    
# Example usage:
if __name__ == "__main__":
    sell_db = SellDatabase()

    # Search for sells by time range
    start_time = input("Enter the start time (YYYY-MM-DD HH:MM:SS): ")
    end_time = input("Enter the end time (YYYY-MM-DD HH:MM:SS): ")
    time_range_sells = sell_db.search_sells_by_time_range(start_time, end_time)

    if time_range_sells:
        print("Sells in the specified time range:")
        for sell in time_range_sells:
            print("Sell Details:")
            for key, value in sell.items():
                print(f"{key}: {value}")
            print("-" * 30)
    else:
        print("No sells found in the specified time range.")

    # Search for sells by product ID
    product_id = input("Enter the Product ID to search: ")
    product_sells = sell_db.search_sells_by_product_id(product_id)

    if product_sells:
        print("Sells for Product ID:", product_id)
        for sell in product_sells:
            print("Sell Details:")
            for key, value in sell.items():
                print(f"{key}: {value}")
            print("-" * 30)
    else:
        print("No sells found for the provided Product ID.")

    # Search for sells by user ID
    user_id = input("Enter the User ID to search: ")
    user_sells = sell_db.search_sells_by_user_id(user_id)

    if user_sells:
        print("Sells for User ID:", user_id)
        for sell in user_sells:
            print("Sell Details:")
            for key, value in sell.items():
                print(f"{key}: {value}")
            print("-" * 30)
    else:
        print("No sells found for the provided User ID.")

    # Close the database connection
    sell_db.close_connection()

