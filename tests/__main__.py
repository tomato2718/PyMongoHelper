from sys import argv

import pytest
from pymongo import MongoClient
from pymongo.collection import Collection

HOST = "0.0.0.0"
PORT = 8017
DATABASE = "testing_database"
COLLECTION = "testing_collection"


class BuildDataBase:
    def __init__(self) -> None:
        client = MongoClient(
            host=HOST,
            port=PORT
        )
        self.database = client.get_database(DATABASE)

    def pytest_sessionstart(self):
        self._create_collection()

    def pytest_sessionfinish(self):
        self._drop_collection()
    
    def _create_collection(self) -> None:
        self.database.create_collection(COLLECTION)
        collection = self.database.get_collection(COLLECTION)
        self._build_data(collection)
    
    @staticmethod
    def _build_data(collection: Collection) -> None:
        data = [
            {'item': 'abc', 'price': 10, 'quantity': 2, 'date': '2014-03-01T08:00:00Z'},
            {'item': 'jkl', 'price': 20, 'quantity': 1, 'date': '2014-03-01T09:00:00Z'},
            {'item': 'xyz', 'price': 5, 'quantity': 10, 'date': '2014-03-15T09:00:00Z'},
            {'item': 'xyz', 'price': 5, 'quantity': 20, 'date': '2014-04-04T11:21:39.736Z'},
            {'item': 'abc', 'price': 10, 'quantity': 10, 'date': '2014-04-04T21:23:13.331Z'},
            {'item': 'def', 'price': 7.5, 'quantity': 5, 'date': '2015-06-04T05:08:13Z'},
            {'item': 'def', 'price': 7.5, 'quantity': 10, 'date': '2015-09-10T08:43:00Z'},
            {'item': 'abc', 'price': 10, 'quantity': 5, 'date': '2016-02-06T20:20:13Z'},
        ]
        collection.insert_many(documents=data)
        
    def _drop_collection(self) -> None:
        self.database.drop_collection(COLLECTION)


if __name__ == '__main__':
    pytest.main(argv[1:], plugins=[BuildDataBase()])