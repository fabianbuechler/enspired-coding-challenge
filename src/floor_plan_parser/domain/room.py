import collections
import dataclasses

from .chair import Chairs, ChairTypeCount


@dataclasses.dataclass
class Room:
    name: str
    chairs: Chairs = dataclasses.field(default_factory=list)

    def count_chair_types(self) -> ChairTypeCount:
        return dict(collections.Counter(self.chairs))


type Rooms = list[Room]
