from typing import Any

from ._base import PyMongoHelper
from .typing import DocumentType

class PyMongoReader(PyMongoHelper[DocumentType]):

    def __call__(self, **filter: Any) -> list[DocumentType]:
        """
        Return a list of query result

        :param Any ``filter``: The document must match
        """
        datas = self._collection.find(filter=filter)
        res = [data for data in datas]
        return res
