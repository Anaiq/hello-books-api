from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    my_beautiful_response_body = "Hello, World!"
    return my_beautiful_response_body

@hello_world_bp.route("/hello/JSON", methods=["GET"])
def say_hello_json():
    return {
        "name" : "QP",
        "message" : "Hey everyone!!",
        "hobbies" : ["Fishing", "Swimming", "Baking"]
    }

@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint(): 
    response_body = {
        "name" : "QP",
        "message" : "Hey everyone!!",
        "hobbies" : ["Fishing", "Swimming", "Baking"]
    }

    new_hobby = "Calligraphy"
    # response_body["hobbies"] + new_hobby #caused TypeError->500Error
    response_body["hobbies"].append(new_hobby) #fixed this error with correct code
    return response_body
