from typing import TextIO

import eel
import mysql.connector

path = r"C:\Users\avida\PycharmProjects\DevOps2702\sela1097\edp\Python_1\app\web_app\web1"
eel.init(path)

eel.start("main.html", size=(700,700))



# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="change-me",
    database="project"
)

 # Retrieve the data from the database
sql = """
USE project;
SELECT
user.*,
product.*,
sell.time
FROM sell
JOIN user ON sell.user_id = user.iduser
JOIN product ON sell.product_id = product.idproduct
WHERE sell.user_id = user.iduser
AND sell.product_id = product.idproduct
"""
           
cursor = conn.cursor()
cursor.execute(sql)
results = cursor.fetchall()
  

                    

   # Create an HTML file
with open("sell.html", "a") as f:

    f.write('<table class="container">')
    f.write("<thead>")
    f.write("<tr>")
    
  for row in results:
      print(row)
      f.write("<tr>")
      for cell in row:
            f.write("<td>" + str(cell) + "</td>")
        f.write("</tr>")
    f.write("</tbody>")
    f.write("</table>")
   
conn.close()