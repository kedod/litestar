from unittest.mock import ANY

from docs.examples.data_transfer_objects.factory.simple_dto_factory_example import app

from litestar.status_codes import HTTP_201_CREATED
from litestar.testing.client import TestClient


def test_create_user() -> None:
    with TestClient(app=app) as client:
        response = client.post(
            "/users",
            json={"name": "Litestar User", "password": "xyz", "created_at": "2023-04-24T00:00:00Z"},
        )

    assert response.status_code == HTTP_201_CREATED
    assert response.json() == {
        "id": ANY,
        "created_at": "2023-04-24T00:00:00Z",
        "name": "Litestar User",
        "password": "xyz",
    }
