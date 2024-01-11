__all__ = [
    "BaseHelper",
    "PyMongoHelper",
]

from types import TracebackType
from typing import Self, Generic
from abc import ABC, abstractmethod

from pymongo.database import Database

from .typing import DocumentType


class BaseHelper(ABC, Generic[DocumentType]):
    """
    Base helper class for pymongo model.

    This class do nothing, just a template help you design db models.

    Usage::

        class MongoReader(BasicHelper):
            _collection = database.get_collection("foo")

            def __call__(self):
                # do some query here
                res = self._collection.find_one()
                return res

        with MongoReader() as reader:
            data = reader()

    """

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

        with MongoReader(database, 'example_collection') as reader:
            data = reader()

    """

    def __init__(self, database: Database[DocumentType], collection_name: str) -> None:
        """
        Constructor method.

        :param Database[DocumentType] database: Instance of pymongo database.
        :param str collection: The name of collection to use.
        """
        self._collection = database.get_collection(collection_name)

    @abstractmethod
    def __call__(self) -> DocumentType:
        pass
