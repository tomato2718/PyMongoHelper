from unittest.mock import MagicMock

import pytest
from pymongo.errors import PyMongoError

from pymongohelper._base import (
    AsyncBaseHelper,
    AsyncMongoHelper,
    BaseHelper,
    PyMongoHelper,
)


class TestBaseHelper:
    class ChildHelper(BaseHelper[MagicMock]):
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
    class ChildHelper(PyMongoHelper[MagicMock]):
        def __call__(self) -> dict:
            return {}

    @classmethod
    def test_init_(cls):
        collection = MagicMock()

        with cls.ChildHelper(collection) as reader:
            assert isinstance(reader._collection, MagicMock)


class TestAsyncBaseHelper:
    class ChildHelper(AsyncBaseHelper[MagicMock]):
        async def __call__(self) -> dict:
            return {}

    @classmethod
    async def test_enter(cls):
        async with cls.ChildHelper() as connection:
            assert isinstance(connection, AsyncBaseHelper)

    @classmethod
    @pytest.mark.parametrize(
        argnames="exc_type",
        argvalues=[
            Exception,
            PyMongoError,
        ],
    )
    async def test_exit(cls, exc_type: type[Exception]):
        with pytest.raises(exc_type):
            async with cls.ChildHelper():
                raise exc_type()


class TestAsyncMongoHelper:
    class ChildHelper(AsyncMongoHelper[MagicMock]):
        async def __call__(self) -> dict:
            return {}

    @classmethod
    async def test_init_(cls):
        collection = MagicMock()

        async with cls.ChildHelper(collection) as reader:
            assert isinstance(reader._collection, MagicMock)
