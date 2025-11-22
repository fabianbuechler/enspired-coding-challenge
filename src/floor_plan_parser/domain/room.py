import collections
import dataclasses

from .chair import Chairs, ChairTypeCount


@dataclasses.dataclass
class Room:
    name: str
    chairs: Chairs

    def count_chair_types(self) -> ChairTypeCount:
        return dict(collections.Counter(self.chairs))


type Rooms = list[Room]
