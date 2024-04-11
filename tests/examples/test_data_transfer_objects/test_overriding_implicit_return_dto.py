from docs.examples.data_transfer_objects.overriding_implicit_return_dto import app

from litestar.status_codes import HTTP_201_CREATED
from litestar.testing.client import TestClient


def test_create_underscored_value() -> None:
    with TestClient(app=app) as client:
        response = client.post("/", json={"bar": "Hello", "_baz": "World!"})

    assert response.status_code == HTTP_201_CREATED
    assert response.json() == {"bar": "Hello"}
