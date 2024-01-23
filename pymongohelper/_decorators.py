__all__ = [
    "UseCollectionDecorator",
]

from typing import Any, Generic, TypeVar

from ._base import AsyncBaseHelper, BaseHelper
from .typing import CollectionType

_SubHelperClass = TypeVar(
    "_SubHelperClass",
    bound=BaseHelper[Any] | AsyncBaseHelper[Any],
)


class UseCollectionDecorator(Generic[CollectionType]):
    """
    Decorator class to add collection into sub class of BaseHelper or AsyncBaseHelper.

    Usage::

        foo_collection = database.get_collection("foo")
        use_foo_collection = UseCollectionDecorator(foo_collection)

        # this will set ``TestHelper._collection`` as ``foo_collection``
        @use_foo_collection
        class TestHelper(BaseHelper):

            def __call__(self) -> dict[str, Any]:
                result = self._collection.find_one()
                return result
    """

    def __init__(
        self,
        collection: CollectionType,
    ) -> None:
        """
        Constructor method.

        :param CollectionType collection: The collection to use.
        """
        self._collection = collection

    def __call__(self, helper_class: type[_SubHelperClass]) -> type[_SubHelperClass]:
        helper_class._collection = self._collection
        return helper_class
