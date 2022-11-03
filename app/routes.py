
from os import abort
from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, abort, make_response, request

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

def validate_id(class_obj,id):
    try:
        id = int(id)
    except:
        abort(make_response({"message":f"{class_obj} {id} invalid"}, 400))

    query_result = class_obj.query.get(id)

    if not query_result:
        abort(make_response({"message":f"{class_obj} {id} not found"}, 404))

    return query_result

@books_bp.route("", methods=["POST"])
def create_book():
    request_body = request.get_json()
    new_book = Book.from_json(request_body)

    db.session.add(new_book)
    db.session.commit()

    return make_response(f"Book {new_book.title} successfully created", 201)

@books_bp.route("", methods=["GET"])
def read_all_books():
    title_query = request.args.get("title")
    if title_query:
        books = Book.query.filter_by(title=title_query)
    else:
        books = Book.query.all()

    books_response = [book.to_dict() for book in books]
    
    return jsonify(books_response)


@books_bp.route("/<book_id>", methods=["GET"])
def read_one_book(book_id):
    book = validate_id(Book, id)
    return book.to_dict()


@books_bp.route("/<book_id>", methods=["PUT"])
def update_book(book_id):
    book = validate_id(Book, id)

    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()

    return make_response(f"Book #{book.id} successfully updated")

@books_bp.route("/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = validate_id(Book, id)

    db.session.delete(book)
    db.session.commit()

    return make_response(f"Book #{book.id} successfully deleted")



