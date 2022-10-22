
from flask import Blueprint, jsonify

hello_world_bp = Blueprint("hello_world_bp", __name__) 

@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    return "Hello, World!"


@hello_world_bp.route("/hello/JSON", methods=["GET"])
def say_hello_json():
    return {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }


@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    return response_body

class Book:

    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description =  description
        
books = [
    Book(1, "Go Away Bugs", "Navigating the world of Error handling"),
    Book(2, "You Wear the Code", "Influence of Technology in Fashion"),
    Book(3, "Through the Palindrome", "A fantasy novel set in a dual reality")
]

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET"])
def get_all_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title" : book.title,
            "description" : book.description
        })

    return jsonify(books_response)
