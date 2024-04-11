from docs.examples.data_transfer_objects.factory.related_items import app

from litestar.status_codes import HTTP_200_OK
from litestar.testing.client import TestClient


def test_update_related_items() -> None:
    with TestClient(app=app) as client:
        response = client.put(
            "/a",
            json={
                "id": "6955e63c-c2bc-4707-8fa4-2144d1764746",
                "b_id": "9cf3518d-7e19-4215-9ec2-e056cac55bf7",
                "b": {"id": "9cf3518d-7e19-4215-9ec2-e056cac55bf7"},
            },
        )

    assert response.status_code == HTTP_200_OK
    assert response.json() == {
        "b_id": "9cf3518d-7e19-4215-9ec2-e056cac55bf7",
        "b": {"id": "9cf3518d-7e19-4215-9ec2-e056cac55bf7"},
        "id": "6955e63c-c2bc-4707-8fa4-2144d1764746",
    }
