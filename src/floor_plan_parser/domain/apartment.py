import collections
import dataclasses
import itertools

from .chair import ChairTypeCount
from .room import Rooms


@dataclasses.dataclass
class Apartment:
    rooms: Rooms

    def count_chair_types(self) -> ChairTypeCount:
        return dict(
            collections.Counter(
                itertools.chain.from_iterable(room.chairs for room in self.rooms)
            )
        )
