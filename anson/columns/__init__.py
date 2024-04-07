from dataclasses import dataclass, field
from typing import Optional, List

from orso.types import OrsoTypes


@dataclass
class BaseColumn:
    name: str
    type: OrsoTypes = OrsoTypes._MISSING_TYPE
    description: Optional[str] = None
    aliases: Optional[List[str]] = field(default_factory=list)  # type: ignore
    nullable: bool = True
    precision: Optional[int] = None
    scale: Optional[int] = None
    metadata: dict = field(default_factory=dict)

    def take(self):
        # copy the items from this row to a new column
        pass

    def to_list(self) -> list:
        pass

    def to_mapped_column(self) -> 'MappedColumn':
        pass
    

class MappedColumn(BaseColumn):
    """
    Mapped columns are backed by a list containing all the values
    """

    data: Union[pyarrow.Array, numpy.Array, anson.Array]


class ConstantColumn(BaseColumn):
    """ """

    pass


class DictionaryColumn(BaseColumn):
    """
    Dictionary columns
    """

    pass


class RLEColumn(BaseColumn):
    pass
