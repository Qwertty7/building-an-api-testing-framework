import falcon
from falcon import testing
import json
import pytest

from api_app.app import api


@pytest.fixture
def client():
    return testing.TestClient(api)


# pytest will inject the object returned by the "client" function
# as an additional parameter.
def test_list_images(client):
    doc = {
        'images': [
            {
                'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
            }
        ]
    }

    response = client.simulate_get('/images')

    assert response.json == doc
    assert response.status == falcon.HTTP_OK


def test_post_image(client):
    doc = {
        'images': [
            {
                'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
            },
            {
                'foo': 'bar'
            }
        ]
    }

    response = client.simulate_post('/images', json={'foo': 'bar'})
    print response.json

    assert response.json == doc
    assert response.status == falcon.HTTP_201