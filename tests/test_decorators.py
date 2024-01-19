from unittest.mock import MagicMock

import pytest

from pymongohelper._base import AsyncBaseHelper, BaseHelper
from pymongohelper._decorators import UseCollectionDecorator


class TestUseCollectionDecorator:
    @staticmethod
    @pytest.fixture(scope="class")
    def use_mock_collection() -> UseCollectionDecorator:
        collection = MagicMock()
        use_mock_collection = UseCollectionDecorator(collection)
        return use_mock_collection

    @staticmethod
    def test_decorator(use_mock_collection: UseCollectionDecorator):
        @use_mock_collection
        class TestHelper(BaseHelper):
            def __call__(self) -> dict:
                return {}

        assert isinstance(TestHelper._collection, MagicMock)

        with TestHelper() as helper:
            assert isinstance(helper._collection, MagicMock)

    @staticmethod
    async def test_async_decorator(use_mock_collection: UseCollectionDecorator):
        @use_mock_collection
        class TestHelper(AsyncBaseHelper):
            async def __call__(self) -> dict:
                return {}

        assert isinstance(TestHelper._collection, MagicMock)

        async with TestHelper() as helper:
            assert isinstance(helper._collection, MagicMock)
