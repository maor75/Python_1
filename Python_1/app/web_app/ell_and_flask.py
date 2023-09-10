import eel
import mysql.connector
from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)

# Initialize Eel with a web folder
eel.init('templates')

# Define the route for displaying data using Flask
@app.route('/')
def get_data():
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

    # Render the HTML template using Flask
    html_content = render_template('sell.html', results=results)

    return html_content

# Define a function to start the Eel app
def start_eel():
    eel.start("main.html", size=(700, 700))

if __name__ == '__main__':
    # Create a Thread to run the Flask app
    flask_thread = Thread(target=app.run, kwargs={'port': 5001})

    # Start the Flask thread
    flask_thread.start()

    # Start the Eel app in the main thread
    start_eel()
