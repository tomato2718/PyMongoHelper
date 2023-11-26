from typing import Any

import pytest
from pymongo.database import Database

from pymongohelper._readers import PyMongoReader


@pytest.mark.parametrize(
        argnames=('expect_count', 'filter'),
        argvalues=[
            (
                3, {"item": "abc"}
            ),
            (
                1, {"item": "abc", "quantity": 10}
            )
        ]
)
def test_PyMongoReader(database: Database[dict[str, Any]], collection: str, expect_count: int, filter: dict[str, Any]):
    data = []
    with PyMongoReader(database=database, collection=collection) as reader:
        data = reader(**filter)

    assert len(data) == expect_count
