#
import mysql.connector

connection = mysql.connector.connect(host="localhost", username="root", password="change-me", database="maor")

def insert_message_into_database(message):
    insert_query = "INSERT INTO messages (message) VALUES (%s)"
    cursor = connection.cursor()
    cursor.execute(insert_query, (message,))
    connection.commit()
    cursor.close()
mas="oriloveedmon"
insert_message_into_database(mas)