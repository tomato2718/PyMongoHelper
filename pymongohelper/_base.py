__all__ = [
    "BaseHelper",
    "PyMongoHelper",
    "AsyncBaseHelper",
    "AsyncMongoHelper",
]

from abc import ABC, abstractmethod
from types import TracebackType
from typing import Any, Generic, Self

from .typing import CollectionType


class BaseHelper(ABC, Generic[CollectionType]):
    """
    Base helper class for pymongo clients.

    This class do nothing, just a template help you design db clients.

    Usage::

        foo_collection = database.get_collection("foo")

        class MongoReader(BaseHelper[Collection[DocumentType]]):
            _collection = foo_collection

            def __call__(self) -> dict[str, Any]:
                # do some query here
                res = self._collection.find_one()
                return res

        with MongoReader() as reader:
            data = reader()

    """

    _collection: CollectionType

    def __init__(self) -> None:
        pass

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[Exception] | None,
        exc_value: Exception | None,
        traceback: TracebackType | None,
    ) -> None:
        pass

    @abstractmethod
    def __call__(self) -> Any:
        pass


class PyMongoHelper(BaseHelper[CollectionType]):
    """
    Helper class with simple constructor method.

    Usage::

        foo_collection = database.get_collection("foo")

        class MongoReader(PyMongoHelper[Collection[DocumentType]]):
            def __call__(self) -> dict[str, Any]:
                # do some query here
                res = self._collection.find_one()
                return res

        with MongoReader(foo_collection) as reader:
            data = reader()

    """

    def __init__(self, collection: CollectionType) -> None:
        """
        Constructor method.

        :param CollectionType collection: The collection to use.
        """
        self._collection = collection


class AsyncBaseHelper(ABC, Generic[CollectionType]):
    """
    Base async helper class for pymongo clients.

    This class do nothing, just a template help you design db clients.

    Usage::

        foo_collection = database.get_collection("foo")

        class AsyncMongoReader(AsyncBaseHelper[AsyncIOMotorCollection[DocumentType]]):
            _collection = foo_collection

            async def __call__(self) -> dict[str, Any]:
                # do some query here
                res = await self._collection.find_one()
                return res

        async with AsyncMongoReader() as reader:
            data = await reader()

    """

    _collection: CollectionType

    def __init__(self) -> None:
        pass

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[Exception] | None,
        exc_value: Exception | None,
        traceback: TracebackType | None,
    ) -> None:
        pass

    @abstractmethod
    async def __call__(self) -> Any:
        pass


class AsyncMongoHelper(AsyncBaseHelper[CollectionType]):
    """
    Helper async class with simple constructor method.

    Usage::

        foo_collection = database.get_collection("foo")

        class MongoReader(AsyncMongoHelper[AsyncIOMotorCollection[DocumentType]]):
            async def __call__(self) -> dict[str, Any]:
                # do some query here
                res = await self._collection.find_one()
                return res

        async with MongoReader(foo_collection) as reader:
            data = await reader()

    """

    def __init__(self, collection: CollectionType) -> None:
        """
        Constructor method.

        :param CollectionType collection: The collection to use.
        """
        self._collection = collection
