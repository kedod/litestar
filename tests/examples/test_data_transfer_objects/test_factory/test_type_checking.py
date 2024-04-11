import pytest

from litestar.exceptions.dto_exceptions import InvalidAnnotationException


def test_create_person_with_id() -> None:
    with pytest.raises(InvalidAnnotationException):
        pass
