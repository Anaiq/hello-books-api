def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_all_books_with_two_records(client, two_saved_books):
    #Act
    response = client.get("/books")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"

    }
    assert response_body[1] == {
        "id": 2,
        "title": "Mountain Book",
        "description": "i luv 2 climb rocks"
    }


def test_get_all_books_with_title_query_matching_none(client, two_saved_books):
    #Act
    data = {"title": "Desert Book"}
    response = client.get("/books", query_string = data)
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_all_books_with_title_query_matching_one(client, two_saved_books):
    pass


def test_get_one_book(client, two_saved_books):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
    }


def test_create_one_book(client):
    # Act
    response = client.post("/books", json={
        "title": "New Book",
        "description": "The Best!"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Book New Book successfully created"
