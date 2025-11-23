import collections
import dataclasses
import itertools

from floor_plan_parser.domain import ChairTypeCount, Rooms


@dataclasses.dataclass
class Apartment:
    rooms: Rooms

    def count_chair_types(self) -> ChairTypeCount:
        return dict(
            collections.Counter(
                itertools.chain.from_iterable(room.chairs for room in self.rooms)
            )
        )
