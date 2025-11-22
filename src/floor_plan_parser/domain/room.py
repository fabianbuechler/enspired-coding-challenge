import dataclasses

from .chair import Chairs, ChairTypeCount


@dataclasses.dataclass
class Room:
    name: str
    chairs: Chairs

    def count_chair_types(self) -> ChairTypeCount:
        raise NotImplementedError()


type Rooms = list[Room]
