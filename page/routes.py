from flask import render_template, request, jsonify

from page import app
from page.data import data
from page.data import Book
from page.forms import ContactForm
from page.models import Author


@app.route('/')
def home():
    return render_template("home.html")


@app.route("/names/<name>")
def name_endpoint(name):
    return f"Hello, {name}"


@app.route("/names")
def names():
    names = ["john", "jenifer", "johan "]
    ages = (1, 2, 3, 4)
    values = {"1": "john", "2": "jenifer", "3": "johan "}
    return render_template("names.html", names=names, ages=ages, values=values)


@app.route("/user")
def user():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        vardas = request.form['vardas']
        return render_template("greetings.html", vardas=vardas)

    return render_template("login.html")


@app.route("/years", methods=['GET', 'POST'])
def years():
    # if request.method == "POST":
    #     year = request.form['year']
    #     result = is_year_leap(year)
    return render_template('years.html')


@app.route("/to_do")
def to_do():
    return render_template("to_do.html")

@app.route("/books")
def books():
    books = data
    return render_template("books.html", books=books)

@app.route("/books/<book>")
def one_book(book):
    result = [b for b in data if b.title == book][0]
    return render_template("book.html", book=result)

@app.route("/api/books/<id>", methods=['GET'])
def author_api(id):
    author = Author.query.get(id)
    if author:
        print(author)
    #     return jsonify(author)
    # else:
    #     return jsonify({'result': "AUTHOR NOT FIND"})


@app.route('/add_article', methods=['GET', 'POST'])
def add_article():
    if request.method == "POST":
        date = request.form["date"]
        author = request.form["author"]
        title = request.form["title"]
        text = request.form["text"]
        age = request.form["age"]
        data.append(
            Book(
                date=date,
                author=author,
                title=title,
                text=text,
                age=age,
            )
        )

    return render_template("add_article.html")

@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    form = ContactForm()
    if form.validate_on_submit():
        return render_template('contact_success.html', form=form)
    return render_template('contact_us.html', form=form)

@app.route("/json", methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you sent': some_json})
    else:
        return jsonify({'about': 'Hello World'})

@app.route("/json/keliamieji/<int:metai>", methods=['GET'])
def keliamieji(metai):
    if True:
        return jsonify({'result': "Keliamieji"})
    else:
        return jsonify({'result': "NE Keliamieji"})


# @app.route('/contact_success', methods=['GET', 'POST'])
# def contact_success():
#     form = ContactForm()
#     if form.validate_on_submit():
#         return render_template('contact_success.html', form=form)
#     return render_template('contact_success')

