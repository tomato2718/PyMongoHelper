__all__ = [
    "BaseHelper",
    "PyMongoHelper",
    "AsyncBaseHelper",
    "AsyncMongoHelper",
]

from abc import ABC, abstractmethod
from types import TracebackType
from typing import Generic, Self

from pymongo.collection import Collection

from .typing import DocumentType


class BaseHelper(ABC, Generic[DocumentType]):
    """
    Base helper class for pymongo model.

    This class do nothing, just a template help you design db models.

    Usage::
        
        foo_collection = database.get_collection("foo")
        
        class MongoReader(BaseHelper):
            _collection = foo_collection

            def __call__(self):
                # do some query here
                res = self._collection.find_one()
                return res

        with MongoReader() as reader:
            data = reader()

    """

    _collection: Collection

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
    def __call__(self) -> DocumentType:
        pass


class PyMongoHelper(BaseHelper[DocumentType]):
    """
    Helper class with simple constructor method.

    Usage::

        class MongoReader(PyMongoHelper[DocumentType]):
            def __call__(self) -> DocumentType:
                # do some query here
                res = self._collection.find_one()
                return res
                
        foo_collection = database.get_collection("foo")

        with MongoReader(foo_collection) as reader:
            data = reader()

    """

    def __init__(self, collection: Collection[DocumentType]) -> None:
        """
        Constructor method.

        :param Collection[DocumentType] collection: The collection to use.
        """
        self._collection = collection


class AsyncBaseHelper(ABC, Generic[DocumentType]):
    """
    Base async helper class for pymongo model.

    This class do nothing, just a template help you design db models.

    Usage::

        foo_collection = database.get_collection("foo")

        class AsyncMongoReader(AsyncBaseHelper):
            _collection = foo_collection

            async def __call__(self):
                # do some query here
                res = await self._collection.find_one()
                return res

        async with AsyncMongoReader() as reader:
            data = await reader()

    """

    _collection: Collection

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
    async def __call__(self) -> DocumentType:
        pass


class AsyncMongoHelper(AsyncBaseHelper[DocumentType]):
    """
    Helper async class with simple constructor method.

    Usage::

        class MongoReader(AsyncMongoHelper[DocumentType]):
            async def __call__(self) -> DocumentType:
                # do some query here
                res = await self._collection.find_one()
                return res

        foo_collection = database.get_collection("foo")

        async with MongoReader(foo_collection) as reader:
            data = await reader()

    """

    def __init__(self, collection: Collection[DocumentType]) -> None:
        """
        Constructor method.

        :param Collection[DocumentType] collection: The collection to use.
        """
        self._collection = collection
