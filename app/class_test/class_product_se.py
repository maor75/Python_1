import mysql.connector

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


if __name__ == "__main__":
 # Example usage:
 product_db = ProductDatabase()

 # Search product by ID
 product_id = input("Enter the product ID to search: ")
 product_result = product_db.search_product_by_id(product_id)

 if product_result:
    product_id, name_product, descripsion = product_result
    print(f"Product ID: {product_id}, Name: {name_product}, Description: {descripsion}")
 else:
    print("No product found for the provided ID.")

 # Search product by name
 product_name = input("Enter the product name to search: ")
 product_results = product_db.search_product_by_name(product_name)

 if product_results:
    print("Matching products by name:")
    for result in product_results:
        product_id, name_product, descripsion = result
        print(f"Product ID: {product_id}, Name: {name_product}, Description: {descripsion}")
 else:
    print("No matching products found for the provided name.")

 # Close the database connection
 product_db.close_connection()
