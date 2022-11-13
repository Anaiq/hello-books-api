from app import db
from app.models.author import Author
from app.models.book import Book
from app.models.genre import Genre
from app.book_routes import validate_model
from flask import Blueprint, jsonify, abort, make_response, request

genres_bp = Blueprint("genres_bp", __name__, url_prefix="/genres")

@genres_bp.route("", methods=["POST"])
def create_genre():
    request_body = request.get_json()

    new_genre = Genre.from_dict(request_body)

    db.session.add(new_genre)
    db.session.commit()

    return make_response(jsonify(f"Genre {new_genre.name} successfully created"))


@genres_bp.route("/", methods=["GET"])
def read_all_genres():
    
    name_query = request.args.get("name")
    if name_query:
        genres = Genre.query.filter_by(name=name_query)
    else:
        genres = Genre.query.all()

    genres_response = []
    for genre in genres:
        genres_response.append(genre.to_dict())
    return jsonify(genres_response)


@genres_bp.route("/<genre_id>/books", methods=["POST"])
def create_book(id):
    genre = validate_model(Genre, id)

    request_body = request.get_json()

    new_book = Book(
        title=request_body["title"],
        description=request_body["description"],
        author_id=request_body["author_id"],
        genres=[genre])
    
    request_body = request.get_json()

    db.session.add(new_book)
    db.session.commit()

    return make_response(jsonify(f"Genre {new_book.title} by {new_book.author} successfully created"))


@genres_bp.route("/id/books", methods=["GET"])
def read_all_books(id):

    genre = validate_model(Genre, id)

    books_response = [books_response.append(book.to_dict()) for book in genre.books]

    return jsonify(books_response)


