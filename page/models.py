from page import db, app
from flask_migrate import Migrate

helper_table = db.Table('author_book',
                        db.Column('book_id', db.Integer, db.ForeignKey('books.id')),
                        db.Column('author_id', db.Integer, db.ForeignKey('authors.id')))


class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message

    def __repr__(self):
        return f'{self.name} - {self.email}'


class Book(db.Model):

    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(150))
    title = db.Column(db.String(300))
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.id'))
    authors = db.relationship('Author', secondary=helper_table, backref='books')

    def __init__(self, author, title, publisher_id):
        self.author = author
        self.title = title
        self.publisher_id = publisher_id

    def __repr__(self):
        return self.title


class Publisher(db.Model):

    __tablename__ = 'publishers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    books = db.relationship('Book', backref='publisher')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Author(db.Model):

    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(150))
    lname = db.Column(db.String(300))

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f'{self.fname} {self.lname}'


class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    phone_number = db.Column(db.Integer)
    orders = db.relationship('Order', backref='customer')

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def __repr__(self):
        return f'{self.name} {self.phone_number}'


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    ingredients = db.Column(db.String(150))
    price = db.Column(db.Float(10))
    orders = db.relationship('Order', backref='product')

    def __init__(self, name, ingredients, price):
        self.name = name
        self.ingredients = ingredients
        self.price = price

    def __repr__(self):
        return f'{self.name} {self.ingredients} {self.price}'


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    quantity = db.Column(db.Integer)

    def __init__(self, customer_id, product_id, quantity):
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity

    def __repr__(self):
        return f'{self.customer_id} {self.product_id} {self.quantity}'


class Offer(db.Model):
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)
    product_id_1 = db.Column(db.Integer, db.ForeignKey('product.id'))
    product_id_2 = db.Column(db.Integer, db.ForeignKey('product.id'))
    price = db.Column(db.Float)

    def __init__(self, product_id_1, product_id_2, price):
        self.product_id_1 = product_id_1
        self.product_id_2 = product_id_2
        self.price = price

    def __repr__(self):
        return f'{self.order_id_1} {self.order_id_2} {self.price}'


Migrate(app, db)
