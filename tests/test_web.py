"""The Django adapter through the test client, with the real composition root."""

import pytest


@pytest.fixture
def client():
    from django.test import Client

    return Client()


def test_index_redirects_to_the_chosen_operation(client):
    assert client.get("/").status_code == 200
    response = client.post("/", {"operation": "grammar"})
    assert response.status_code == 302 and response["Location"] == "/grammar"


@pytest.mark.parametrize(
    "path, expected", [("/normal", "котами: кот"), ("/grammar", "котами: СУЩ")]
)
def test_text_operations(client, path, expected):
    assert client.get(path).status_code == 200
    body = client.post(path, {"text": "котами"}).content.decode()
    assert expected in body


def test_inflect(client):
    body = client.post(
        "/inflect", {"text": "кот", "case": "gent", "number": "plur"}
    ).content.decode()
    assert "кот: котов" in body


def test_invalid_input_shows_the_form_again(client):
    response = client.post("/inflect", {"text": "кот", "case": "bogus", "number": "plur"})
    assert response.status_code == 200 and "котов" not in response.content.decode()
