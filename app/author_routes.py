from app import db
from app.models.author import Author
from app.models.book import Book
from app.book_routes import validate_model
from flask import Blueprint, jsonify, abort, make_response, request

authors_bp = Blueprint("authors_bp", __name__, url_prefix="/authors")

@authors_bp.route("", methods=["POST"])
def create_author():
    request_body = request.get_json()
    new_author = Author.from_dict(request_body)

    db.session.add(new_author)
    db.session.commit()

    return make_response(jsonify(f"Author {new_author.name} successfully created"), 201)

#send a request to create a new book and connect it to an author already found in the database
@authors_bp.route("/<author_id>/books", methods=["POST"])
def create_book_associated_with_author(author_id):
    author = validate_model(Author, author_id)

    request_body = request.get_json()
    new_book = Book(
        title=request_body['title'],
        description=request_body["description"],
        author=author
    )

    db.session.add(new_book)
    db.session.commit()

    return make_response(jsonify(f"Book {new_book.title} by {new_book.author.name} successfully created"), 201)


@authors_bp.route("", methods=["GET"])
def read_all_authors():
    name_query = request.args.get("name")
    if name_query:
        authors = Author.query.filter_by(name=name_query)
    else:
        authors = Author.query.all()

    authors_response = []
    for author in authors:
        authors_response.append(author.to_dict())

    return jsonify(authors_response)


#send a request to read all books by a particular author in the database.
@authors_bp.route("/<author_id>/books", methods=["GET"])
def read_all_books_from_author(author_id):
    author = validate_model(Author, author_id)

    books_response = []
    for book in author.books:
        books_response.append(book.to_dict())
    return jsonify(books_response)

@authors_bp.route("/<author_id>", methods=["GET"])
def read_one_author(author_id):
    author = validate_model(Author, author_id)
    return author.to_dict()