from app import db
from app.models.author import Author
from flask import Blueprint, jsonify, abort, make_response, request

authors_bp = Blueprint("authors_bp", __name__, url_prefix="/authors")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))

    return model

@authors_bp.route("", methods=["POST"])
def create_author():
    request_body = request.get_json()
    new_author = Author.from_dict(request_body)

    db.session.add(new_author)
    db.session.commit()

    return make_response(jsonify(f"Author {new_author.name} successfully created"), 201)

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

@authors_bp.route("/<author_id>", methods=["GET"])
def read_one_author(author_id):
    author = validate_model(Author, author_id)
    return author.to_dict()