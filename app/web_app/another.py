import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="edmon",
    database="project"
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Define the SQL query
sql = """
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

# Execute the SQL query
cursor.execute(sql)

# Fetch all the results
results = cursor.fetchall()

# Display the results in the terminal
for row in results:
    print(row)

# Close the cursor and database connection
cursor.close()
conn.close()