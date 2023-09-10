import mysql.connector
from datetime import datetime

connection = mysql.connector.connect(host="localhost", user="root", password="change-me", database="project")

def insert_message_into_database(id, name, lname):
    select_query = "SELECT iduser FROM user WHERE iduser = %s"
    update_query = "UPDATE user SET last_name = %s, first_name = %s WHERE iduser = %s"
    insert_query = "INSERT INTO user (iduser, last_name, first_name) VALUES (%s, %s, %s)"

    cursor = connection.cursor()

    cursor.execute(select_query, (id,))
    existing_record = cursor.fetchone()

    if existing_record:
        cursor.execute(update_query, (lname, name, id))
    else:
        cursor.execute(insert_query, (id, lname, name))

    connection.commit()
    cursor.close()

id = "4"
name = "ori"
lname = "123ed"
insert_message_into_database(id, name, lname)
