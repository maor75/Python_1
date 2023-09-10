import eel 
import mysql.connector

path = r"C:\Users\avita\OneDrive\Desktop\Python_1\app\web_app\web1"
eel.init(path)

eel.start("main.html", size=(700,700))



# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="edmon",
    database="project"
)

# Retrieve the data from the database
sql = """
SELECT *
FROM sell
JOIN user ON sell.user_id = user.iduser
JOIN product ON sell.product = product.idproduct
"""
           
cursor = conn.cursor()
cursor.execute(sql)
print(sql)
# Create an HTML table
table_data = []
for row in cursor:
    table_data.append(row)

# Close the connection to the MySQL database
conn.close()

# Create an HTML file
with open("sell.html", "w") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <style>@charset "UTF-8";
@import url(https://fonts.googleapis.com/css?family=Open+Sans:300,400,700);

body {
  font-family: 'Open Sans', sans-serif;
  font-weight: 300;
  line-height: 1.42em;
  color:#A7A1AE;
  background-color:#1F2739;
}

h1 {
  font-size:3em; 
  font-weight: 300;
  line-height:1em;
  text-align: center;
  color: #4DC3FA;
}

h2 {
  font-size:1em; 
  font-weight: 300;
  text-align: center;
  display: block;
  line-height:1em;
  padding-bottom: 2em;
  color: #FB667A;
}

h2 a {
  font-weight: 700;
  text-transform: uppercase;
  color: #FB667A;
  text-decoration: none;
}

.blue { color: #185875; }
.yellow { color: #FFF842; }

.container th h1 {
	  font-weight: bold;
	  font-size: 1em;
  text-align: left;
  color: #185875;
}

.container td {
	  font-weight: normal;
	  font-size: 1em;
  -webkit-box-shadow: 0 2px 2px -2px #0E1119;
	   -moz-box-shadow: 0 2px 2px -2px #0E1119;
	        box-shadow: 0 2px 2px -2px #0E1119;
}

.container {
	  text-align: left;
	  overflow: hidden;
	  width: 80%;
	  margin: 0 auto;
  display: table;
  padding: 0 0 8em 0;
}

.container td, .container th {
	  padding-bottom: 2%;
	  padding-top: 2%;
  padding-left:2%;  
}

/* Background-color of the odd rows */
.container tr:nth-child(odd) {
	  background-color: #323C50;
}

/* Background-color of the even rows */
.container tr:nth-child(even) {
	  background-color: #2C3446;
}

.container th {
	  background-color: #1F2739;
}

.container td:first-child { color: #FB667A; }

.container tr:hover {
   background-color: #464A52;
-webkit-box-shadow: 0 6px 6px -6px #0E1119;
	   -moz-box-shadow: 0 6px 6px -6px #0E1119;
	        box-shadow: 0 6px 6px -6px #0E1119;
}

.container td:hover {
  background-color: #FFF842;
  color: #403E10;
  font-weight: bold;
  
  box-shadow: #7F7C21 -1px 1px, #7F7C21 -2px 2px, #7F7C21 -3px 3px, #7F7C21 -4px 4px, #7F7C21 -5px 5px, #7F7C21 -6px 6px;
  transform: translate3d(6px, -6px, 0);
  
  transition-delay: 0s;
	  transition-duration: 0.4s;
	  transition-property: all;
  transition-timing-function: line;
}

@media (max-width: 800px) {
.container td:nth-child(4),
.container th:nth-child(4) { display: none; }
}
</style>""")
    f.write("""<h1><span class="blue">&lt;</span>Table<span class="blue">&gt;</span> <span class="yellow">Responsive</pan></h1>
    <h2>Created with love by <a href="https://github.com/pablorgarcia" target="_blank">Pablo García</a></h2>
  """)
    f.write('<table class="container">')
    f.write("<thead>")
    f.write("<tr>")
    for column in cursor.column_names:
        f.write("<th><h1>" + column + "</h1></th>")
    f.write("</tr>")
    f.write("</thead>")
    f.write("<tbody>")
    for row in table_data:
        f.write("<tr>")
        for cell in row:
            f.write("<td>" + cell + "</td>")
        f.write("</tr>")
    f.write("</tbody>")
    f.write("</table>")
   