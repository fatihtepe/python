# Import Flask modules
from flask import Flask, jsonify, abort, request, make_response
from flask_sqlalchemy import SQLAlchemy

# Create an object named app
app = Flask(__name__)

# Configure sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./bookstore.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

# Write a function named `init_bookstore_db` which initilazes the bookstore db
# Create books table within sqlite db and populate with sample data
# Execute the code below only once.
def init_bookstore_db():
    drop_table = 'DROP TABLE IF EXISTS books;'
    books_table = """
    CREATE TABLE books(
    book_id INTEGER PRIMARY KEY,
    title VARCHAR NOT NULL,
    author VARCHAR,
    is_sold BOOLEAN NOT NULL DEFAULT 0 CHECK(is_sold IN(0,1)));
    """
    data = """
    INSERT INTO books (title, author, is_sold)
    VALUES
        ("Where the Crawdads Sing", "Delia Owens", 1 ),
        ("The Vanishing Half: A Novel", "Brit Bennett", 0),
        ("1st Case", "James Patterson, Chris Tebbetts", 0);
    """
    db.session.execute(drop_table)
    db.session.execute(books_table)
    db.session.execute(data)
    db.session.commit()

# Write a function named `get_all_books` which gets all books from the books table in the db,
# and return result as list of dictionary
# `[{'book_id': 1, 'title':'XXXX', 'author': 'XXXXXX', 'is_sold': 'Yes' or 'No'} ]`.
def get_all_books():
    query = """
    SELECT * FROM books;
    """
    result = db.session.execute(query)
    books =[{'book_id':row[0], 'title':row[1], 'author':row[2], 'is_sold': bool(row[3])} for row in result]
    return books

# Write a function named `find_book` which finds book using book_id from the books table in the db,
# and return result as list of dictionary
# `[{'book_id': 1, 'title':'XXXX', 'author': 'XXXXXX', 'is_sold': 'Yes' or 'No'} ]`.
def find_book(id):
    query = f"""
    SELECT * FROM books WHERE book_id={id};
    """
    row = db.session.execute(query).first()
    book = None
    if row is not None:
        book = {'book_id':row[0], 'title':row[1], 'author':row[2], 'is_sold': bool(row[3])}
    return book


# Write a function named `insert_book` which inserts book into the books table in the db,
# and return the newly added book as dictionary
# `[{'book_id': 1, 'title':'XXXX', 'author': 'XXXXXX', 'is_sold': 'Yes' or 'No'} ]`.
def insert_book(title, author):
    insert = f"""
    INSERT INTO books (title, author)
    VALUES ('{title}', '{author}');
    """
    result = db.session.execute(insert)
    db.session.commit()

    query = f"""
    SELECT * FROM books WHERE book_id={result.lastrowid};
    """
    row = db.session.execute(query).first()

    return {'book_id':row[0], 'title':row[1], 'author':row[2], 'is_sold': bool(row[3])}

# Write a function named `change_book` which updates book into the books table in the db,
# and return updated added book as dictionary
# `[{'book_id': 1, 'title':'XXXX', 'author': 'XXXXXX', 'is_sold': 'Yes' or 'No'} ]`.
def change_book(book):
    update = f"""
    UPDATE books
    SET title='{book['title']}', author = '{book['author']}', is_sold = {book['is_sold']}
    WHERE book_id= {book['book_id']};
    """
    result = db.session.execute(update)
    db.session.commit()

    query = f"""
    SELECT * FROM books WHERE book_id={book['book_id']};
    """
    row = db.session.execute(query).first()
    return {'book_id':row[0], 'title':row[1], 'author':row[2], 'is_sold': bool(row[3])}

# Write a function named `remove_book` which removes book from the books table in the db,
# and returns True if successfully deleted or False.
def remove_book(book):
    delete = f"""
    DELETE FROM books
    WHERE book_id= {book['book_id']};
    """
    result = db.session.execute(delete)
    db.session.commit()

    query = f"""
    SELECT * FROM books WHERE book_id={book['book_id']};
    """
    row = db.session.execute(query).first()
    return True if row is None else False


# Write a function named `home` which returns 'Welcome to the Callahan's Bookstore API Service',
# and assign to the static route of ('/')
@app.route('/')
def home():
    return "Welcome to Callahan's Bookstore API Service"

# Write a function named `get_books` which returns all books in JSON format for `GET`,
# and assign to the static route of ('/books')
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books':get_all_books()})


# Write a function named `get_books` which returns the book with given book_id in JSON format for `GET`,
# and assign to the static route of ('/books/<int:book_id>')
@app.route('/books/<int:book_id>', methods = ['GET'])
def get_book(book_id):
    book = find_book(book_id)
    if book == None:
        abort(404)
    return jsonify({'book found': book})

# Write a function named `add_book` which adds new book using `POST` methods,
# and assign to the static route of ('/books')
@app.route('/books', methods=['POST'])
def add_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    return jsonify({'newly added book':insert_book(request.json['title'], request.json.get('author', ''))}), 201

# Write a function named `update_book` which updates an existing book using `PUT` method,
# and assign to the static route of ('/books/<int:book_id>')
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = find_book(book_id)
    if book == None:
        abort(404)
    if not request.json:
        abort(400)
    book['title'] = request.json.get('title', book['title'])
    book['author'] = request.json.get('author', book['author'])
    book['is_sold'] = int(request.json.get('is_sold', int(book['is_sold'])))
    return jsonify({'updated book': change_book(book)})

# Write a function named `delete_book` which updates an existing book using `DELETE` method,
# and assign to the static route of ('/books/<int:book_id>')
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = find_book(book_id)
    if book == None:
        abort(404)
    return jsonify({'result':remove_book(book)})

# Write a function named `not_found` for handling 404 errors which returns 'Not found' in JSON format.
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# Write a function named `bad_request` for handling 400 errors which returns 'Bad Request' in JSON format.
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


# Add a statement to run the Flask application which can be reached from any host on port 80.
if __name__== '__main__':
    init_bookstore_db()
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)