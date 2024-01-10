import pytest
from unittest.mock import MagicMock
from pymongo.database import Database
from pymongo.errors import PyMongoError

from pymongohelper._base import PyMongoHelper


@pytest.fixture(scope="module")
def database() -> Database:
    database = MagicMock()
    return database


class TestPyMongoHelper:
    @staticmethod
    @pytest.fixture(scope="class")
    def child_instance(database: Database) -> PyMongoHelper:
        class Child(PyMongoHelper):
            def __call__(self) -> dict:
                return {}

        return Child(database=database, collection="foo")

    @staticmethod
    def test_enter(child_instance: PyMongoHelper):
        with child_instance as connection:
            assert isinstance(connection, PyMongoHelper)

    @staticmethod
    @pytest.mark.parametrize(argnames="exc_type", argvalues=[Exception, PyMongoError])
    def test_exit(child_instance: PyMongoHelper, exc_type: type[Exception]):
        with child_instance, pytest.raises(exc_type):
            raise exc_type()
