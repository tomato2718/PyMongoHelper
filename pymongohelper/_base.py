from types import TracebackType
from typing import Self, Generic
from abc import ABC, abstractmethod

from pymongo.database import Database
from pymongo.errors import PyMongoError

from .typing import DocumentType


class PyMongoHelper(ABC, Generic[DocumentType]):
    """
    Base class of ``PyMongoHelper``.

    Usage::

        class MongoReader(PyMongoHelper):
            def __call__(self):
                # do some query here
                res = self._collection.find_one()
                return res

        with MongoReader(database, 'example_collection') as reader:
            data = reader()
    
    """
    def __init__(self, database: Database[DocumentType], collection: str) -> None:
        self._collection = database.get_collection(collection)

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[Exception] | None,
        exc_value: Exception | None,
        traceback: TracebackType | None,
    ) -> bool:
        if exc_type == PyMongoError:
            return False
        elif exc_type == Exception:
            return False
        else:
            return True

    @abstractmethod
    def __call__(self) -> DocumentType:
        pass