from unittest.mock import ANY

from docs.examples.data_transfer_objects.factory.renaming_all_fields import app

from litestar.status_codes import HTTP_201_CREATED
from litestar.testing.client import TestClient


def test_create_user() -> None:
    with TestClient(app=app) as client:
        response = client.post(
            "/users",
            json={"firstName": "Litestar User", "password": "xyz", "createdAt": "2023-04-24T00:00:00Z"},
        )

    assert response.status_code == HTTP_201_CREATED
    assert response.json() == {"createdAt": "0001-01-01T00:00:00", "id": ANY, "firstName": "Litestar User"}
