.. template documentation master file, created by
   sphinx-quickstart on Sun Jul  9 16:38:41 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

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

- ``pymongo==4.6.1``

Setup
-------------

Installation
^^^^^^^^^^^^^

- Install with Python pip

.. code-block:: shell

   pip install pymongohelper-0.1.0-py3-none-any.whl


Usage
-------------

Import as a module
^^^^^^^^^^^^^^^^^^

- Import this Project as a module.

.. code-block:: python

   from typing import Any

   from pymongo import MongoClient
   from pymongohelper import BaseHelper, UseCollectionDecorator

   # configure your own pymongo client
   client = MongoClient(
      host=URI,
   )
   database = client.get_database(DATABASE_NAME)

   # create decorators base on collections
   use_foo_collection = UseCollectionDecorator(
      database=database,
      collection_name=COLLECTION_NAME,
   )

   # apply decorators to your database models
   @use_foo_collection
   class MongoReader(BaseHelper):
      def __call__(self) -> dict[str, Any]:
         result = self._collection.find_one({})
         return result

   # use the database models
   with MongoReader() as read_data:
      result = read_data()


Run the tests
--------------

- Unit tests

.. code-block:: shell

   >>> python -m pytest


Support
--------------

Author
^^^^^^^^^^^^^^

- ``yveschen2718@gmail.com``

Maintainer
^^^^^^^^^^^^^^

- ``yveschen2718@gmail.com``