from docs.examples.data_transfer_objects.factory.dto_data_problem_statement import app

from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR
from litestar.testing.client import TestClient


def test_create_person() -> None:
    with TestClient(app=app) as client:
        response = client.post("/person", json={"name": "Mr Sunglass", "age": 30})

    assert response.status_code == HTTP_500_INTERNAL_SERVER_ERROR
    assert response.json() == {"detail": "Internal Server Error", "status_code": 500}
