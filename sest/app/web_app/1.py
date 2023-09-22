from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder=r'C:\Users\avida\PycharmProjects\DevOps2702\sela1097\edp\sest\templates')


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

@app.route('/')
def index():
    # Retrieve a list of products from the 'product' table
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_details(product_id):
    # Retrieve product details from the 'product' table based on the product_id
    product = Product.query.get(product_id)
    if product:
        # Retrieve sale content for the product from the 'sale_content' table
        sale_content = SaleContent.query.filter_by(product_id=product_id).all()
        return render_template('product_details.html', product=product, sale_content=sale_content)
    else:
        return "Product not found"

if __name__ == '__main__':
    # Create database tables (if not already created) within the application context
    with app.app_context():
        db.create_all()
    app.run(debug=True)
