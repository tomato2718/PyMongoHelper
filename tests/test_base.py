from unittest.mock import MagicMock

import pytest
from pymongo.errors import PyMongoError

from pymongohelper._base import BaseHelper, PyMongoHelper


class TestBasicHelper:
    class ChildHelper(BaseHelper):
        def __call__(self) -> dict:
            return {}

    @classmethod
    def test_enter(cls):
        with cls.ChildHelper() as connection:
            assert isinstance(connection, BaseHelper)

    @classmethod
    @pytest.mark.parametrize(
        argnames="exc_type",
        argvalues=[
            Exception,
            PyMongoError,
        ],
    )
    def test_exit(cls, exc_type: type[Exception]):
        with (
            cls.ChildHelper(),
            pytest.raises(exc_type),
        ):
            raise exc_type()

class TestPyMongoHelper:
    class ChildHelper(PyMongoHelper):
        def __call__(self) -> dict:
            return {}
        
    @classmethod
    def test_init_(cls):
        database = MagicMock()
        collection_name = "MockCollection"

        with cls.ChildHelper(database=database, collection_name=collection_name) as reader:
            assert isinstance(reader._collection, MagicMock)