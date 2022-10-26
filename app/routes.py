from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, abort, make_response, request

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.route("", methods=['Post'])
def get_all_books():
    request_body = request.get_json()
    new_book = Book(title=request_body['title'],
                    author=request_body['author'],
                    year_published=request_body['year_published'],
                    descrtiption=request_body['description'])

    db.session.add(new_book)
    db.session.commit()

    return make_response(f"Book {new_book.title} successfully created", 201)