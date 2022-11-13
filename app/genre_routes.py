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


@genres_bp.route("", methods=["GET"])
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