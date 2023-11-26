from typing import Any, TypeAlias

import pytest
from pymongo import MongoClient
from pymongo.database import Database

T: TypeAlias = dict[str, Any]

@pytest.fixture(scope="session")
def client() -> MongoClient[T]:
    client = MongoClient(host="0.0.0.0", port=8017, document_class=T)
    return client


@pytest.fixture(scope="session")
def database(client: MongoClient[T]) -> Database[T]:
    DATABASE_NAME = "testing_database"
    database = client.get_database(DATABASE_NAME)
    return database

@pytest.fixture(scope="session")
def collection() -> str:
    COLLECTION_NAME = "testing_collection"
    return COLLECTION_NAME