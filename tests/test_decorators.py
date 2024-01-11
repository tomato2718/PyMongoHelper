from unittest.mock import MagicMock

from pymongohelper._base import BaseHelper
from pymongohelper._decorators import UseCollectionDecorator


class TestUseCollectionDecorator:
    def test_decorator(self):
        database = MagicMock()
        collection_name = "mock_collection"

        use_mock_collection = UseCollectionDecorator(
            database=database,
            collection_name=collection_name,
        )

        @use_mock_collection
        class TestHelper(BaseHelper):
            def __call__(self) -> dict:
                return {}

        assert isinstance(TestHelper._collection, MagicMock)

        with TestHelper() as helper:
            assert isinstance(helper._collection, MagicMock)
