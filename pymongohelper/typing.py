"""
Typing module of pymongohelper
"""

__all__ = ["DocumentType", "CollectionType"]

from typing import TypeVar, TypeAlias, Mapping, Any

DocumentType: TypeAlias = Mapping[str, Any]
CollectionType = TypeVar("CollectionType")
