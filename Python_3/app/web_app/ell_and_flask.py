import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)

# Define the route for displaying data from the 'sales' table
@app.route('/')
def navigationbar1():
    return render_template('navigationbar1.html')
# Define routes for other HTML templates
@app.route('/nav2')
def nav2():
    return render_template('nav2.html')

@app.route('/nav3')
def nav3():
    return render_template('nav3.html')

@app.route('/nav4')
def get_data():
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="change-me",
            database="app1"
        )

        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Define the SQL query to fetch data from the 'sales' table
        sql = """
            SELECT
                s.sale_id,
                CONCAT(st.stuff_name, ' ', st.last_name) AS stuff_name_last_name,
                CONCAT(c.costumer_name, ' ', c.last_name) AS costumer_name_last_name,
                s.price,
                s.date
            FROM
                sales AS s
            JOIN
                costumers AS c ON s.costumer_id = c.costumer_id
            JOIN
                stuff AS st ON s.stuff_id = st.stuff_id;
            """

        # Execute the SQL query
        cursor.execute(sql)

        # Fetch all the results
        results = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        conn.close()

        # Render the HTML template using Flask
        return render_template('nav4.html', results=results)

    except mysql.connector.Error as e:
        # Handle database errors here
        return f"Database Error: {str(e)}"


@app.route('/nav5')
def nav5():
    return render_template('nav5.html')

if __name__ == '__main__':
    # Start the Flask app
    app.run(port=5001)
