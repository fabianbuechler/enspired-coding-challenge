import enum
from collections.abc import Iterable
from typing import Protocol

type ChairTypeCount = dict[ChairType, int]


class ChairType(enum.Enum):
    WOODEN = "W"
    PLASTIC = "P"
    SOFA = "S"
    CHINA = "C"


type Chairs = Iterable[ChairType]


class ChairContainer(Protocol):
    chairs: Chairs

    def count_chair_types(self) -> ChairTypeCount: ...
