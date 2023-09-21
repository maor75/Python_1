import mysql.connector
from flask import Flask, render_template
import webbrowser  # Import the webbrowser module

app = Flask(__name__)

@app.route('/')
def navigationbar1():
    return render_template('navigationbar1.html')

@app.route('/nav2')
def get_data_nav2():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="change-me",
            database="app1"
        )

        cursor = conn.cursor()

        sql = """
        SELECT p.product_name, p.productc_description AS product_description, s.amount
        FROM supplies AS s
        JOIN product AS p ON s.product_id = p.product_id;
        """

        cursor.execute(sql)

        results = cursor.fetchall()

        cursor.close()
        conn.close()

        return render_template('nav2.html', results=results)

    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/nav3')
def nav3():
    return render_template('nav3.html')

@app.route('/nav4')
def get_data_nav4():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="change-me",
            database="app1"
        )

        cursor = conn.cursor()

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

        cursor.execute(sql)

        results = cursor.fetchall()

        cursor.close()
        conn.close()

        return render_template('nav4.html', results=results)

    except mysql.connector.Error as e:
        return f"Database Error: {str(e)}"

@app.route('/nav5')
def nav5():
    return render_template('nav5.html')

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5001')  # Open the default web browser
    app.run(port=5001)
