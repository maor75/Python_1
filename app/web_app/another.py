from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Configure the MySQL database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="edmon",
    database="project"
)

@app.route('/')
def display_data():
    # Retrieve data from the database
    cursor = conn.cursor()
    sql = """
    SELECT *
    FROM user
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()

    # Pass the data to the HTML template
    return render_template('index.html', data=rows)

if __name__ == '__main__':
    app.run(debug=True)
