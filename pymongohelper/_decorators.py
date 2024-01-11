__all__ = [
    "UseCollectionDecorator",
]

from typing import Any, TypeVar

from pymongo.database import Database

from ._base import BaseHelper
from .typing import DocumentType


_SubHelperClass = TypeVar("_SubHelperClass", bound=BaseHelper[Any])


class UseCollectionDecorator:
    """
    Decorator class to add collection into sub class of BaseHelper.

    Usage::

        use_mock_collection = UseCollectionDecorator(
            database=database,
            collection_name=collection_name,
        )

        # this will add ``database.collection`` into TestHelper class
        @use_mock_collection
        class TestHelper(BaseHelper):
            def __call__(self) -> dict:
                result = self._collection.findone()
                return result
    """

    def __init__(
        self,
        database: Database[DocumentType],
        collection_name: str,
    ) -> None:
        """
        Constructor method.

        :param Database[DocumentType] database: Instance of pymongo database.
        :param str collection: The name of collection to use.
        """
        self._database = database
        self._collection_name = collection_name

    def __call__(self, helper_class: type[_SubHelperClass]) -> type[_SubHelperClass]:
        helper_class._collection = self._database.get_collection(self._collection_name)

        return helper_class
