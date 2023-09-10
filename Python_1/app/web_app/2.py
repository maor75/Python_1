from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def display_data():
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="change-me",
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

    # Close the cursor and database connection
    cursor.close()
    conn.close()

    return render_template('sell.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
