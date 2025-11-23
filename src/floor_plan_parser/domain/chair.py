import enum
from typing import Protocol

type ChairTypeCount = dict[ChairType, int]


class ChairType(enum.Enum):
    WOODEN = "W"
    PLASTIC = "P"
    SOFA = "S"
    CHINA = "C"


type Chairs = list[ChairType]


class ChairContainer(Protocol):
    chairs: Chairs

    def count_chair_types(self) -> ChairTypeCount: ...
