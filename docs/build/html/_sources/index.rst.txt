PyMongoHelper Documentation
====================================

Contents
------------------------------------

.. toctree::
    :maxdepth: 2

    modules

Summary
-------------

A library help you design pymongo client more clean.


Requirements
-------------

System
^^^^^^^^^^^^^

- ``python>=3.10``

Python
^^^^^^^^^^^^^

- ``None``

Setup
-------------

Installation
^^^^^^^^^^^^^

- Install with Python pip

.. code-block:: shell

    pip install pymongohelper-0.4.0-py3-none-any.whl


Usage
-------------

Import as a module
^^^^^^^^^^^^^^^^^^

- Import this Project as a module.

.. code-block:: python

    from typing import Any

    from pymongo import MongoClient
    from pymongo.collection import Collection
    from pymongohelper import BaseHelper, UseCollectionDecorator

    # configure your own pymongo client
    client = MongoClient(
        host="URI",
        document_class=dict[str, Any]
    )
    database = client.get_database(DATABASE_NAME)
    collection = database.get_collection(COLLLECTION_NAME)

    # create decorators base on collections
    use_foo_collection = UseCollectionDecorator(collection)

    # apply decorators to your database querying objects
    @use_foo_collection
    class MongoReader(BaseHelper[Collection[dict[str, Any]]]):
        def __call__(self) -> dict[str, Any]:
            result = self._collection.find_one({})
            return result or {}

    # use the database querying objects
    with MongoReader() as read_data:
        result = read_data()


Run the tests
--------------

- Unit tests

.. code-block:: shell

    python -m pytest


Support
--------------

Author
^^^^^^^^^^^^^^

- ``yveschen2718@gmail.com``

Maintainer
^^^^^^^^^^^^^^

- ``yveschen2718@gmail.com``