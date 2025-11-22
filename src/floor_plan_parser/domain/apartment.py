import dataclasses

from .chair import Chairs, ChairTypeCount
from .room import Rooms


@dataclasses.dataclass
class Apartment:
    rooms: Rooms

    @property
    def chairs(self) -> Chairs:
        raise NotImplementedError()

    def count_chair_types(self) -> ChairTypeCount:
        raise NotImplementedError()
