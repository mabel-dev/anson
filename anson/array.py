from typing import Iterable

from orso.types import OrsoTypes

from anson.constants import Compression


class Array:
    """
    This is the array that backs columns
    """

    def __init__(
        self,
        values: Iterable,
        atype: OrsoTypes = OrsoTypes._MISSING_TYPE,
        compression: Compression = Compression.NONE,
    ):
        pass

    def take(items:Iterable[int]=None) -> "Array":
        """
        Create a new Array of the items in the items list
        """
        pass

    def decompress(self) -> "Array":
        """
        decompress an Array
        """
        pass