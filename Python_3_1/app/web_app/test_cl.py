import mysql.connector
from flask import Flask, render_template, jsonify
import webbrowser
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,
            template_folder=r'C:\Users\avida\PycharmProjects\DevOps2702\sela1097\edp\Python_3_1\app\web_app\templates')

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:change-me@localhost/app1'
db = SQLAlchemy(app)


# Define database models
class Product(db.Model):
    __tablename__ = 'product'
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(45), nullable=False)
    productc_description = db.Column(db.String(45), nullable=False)
    price = db.Column(db.Integer, nullable=False)


class SaleContent(db.Model):
    __tablename__ = 'sale_content'
    sale_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)


@app.route('/get_sale_details/<int:sale_id>')
def get_sale_details(sale_id):
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="change-me",
            database="app1"
        )

        cursor = conn.cursor()

        # Define the SQL query to fetch additional information based on sale_id
        sql = """
            SELECT product_name, costumer_name
            FROM sales
            WHERE sale_id = %s;
        """

        cursor.execute(sql, (sale_id,))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if result:
            # Convert the result to a dictionary for JSON response
            sale_details = {
                'product_name': result[0],
                'costumer_name': result[1],
            }
            return jsonify(sale_details)
        else:
            return jsonify({'error': 'Sale not found'}), 404

    except mysql.connector.Error as e:
        return jsonify({'error': str(e)}), 500


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
        SELECT p.product_id, p.product_name, p.productc_description AS product_description, s.amount
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
def get_data_nav5():
    return render_template('nav5.html')


# Import Flask and other necessary modules
# ...

@app.route('/product/<int:product_id>')
def product_details(product_id):
    # Retrieve product details from the 'Product' model based on the product_id
    product = Product.query.get(product_id)
    if product:
        # Retrieve sale content for the product from the 'SaleContent' model
        sale_content = SaleContent.query.filter_by(product_id=product_id).all()
        return render_template('nav5', product=product, sale_content=sale_content)
    else:
        return "Product not found"



if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5001')
    app.run(port=5001)
