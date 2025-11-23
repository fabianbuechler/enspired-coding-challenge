import operator
import re
from collections.abc import Iterable, Iterator

import numpy as np

from floor_plan_parser.domain import ChairType, Room

from .apartment import Apartment

type Coordinate = tuple[int, int]  # y, x


class FloorPlan:
    _re_room_marker: re.Pattern = re.compile(r"\((?P<name>[\w\s]+)\)", re.ASCII)

    _WALL_CHARACTERS = {"|", "-", "+", "\\", "/"}
    _CHAIR_MARKERS = {chair_type.value for chair_type in ChairType}

    def __init__(self, floor_plan_ascii: str):
        self.ascii_lines = floor_plan_ascii.splitlines()
        width = max(len(line) for line in self.ascii_lines)
        self.map = np.genfromtxt(self.ascii_lines, dtype="U1", delimiter=[1] * width)
        self.height, self.width = self.map.shape

    def _find_room_marker_positions(self) -> Iterable[tuple[str, Coordinate]]:
        room_markers: list[tuple[str, Coordinate]] = []
        for y, line in enumerate(self.ascii_lines):
            for match in self._re_room_marker.finditer(line):
                start, end = match.span("name")
                x = (start + end) // 2
                room_markers.append((match.group("name"), (y, x)))
        return sorted(room_markers, key=operator.itemgetter(1))

    def _find_chairs_within_room(
        self, x: int, y: int, visited: set[Coordinate]
    ) -> Iterator[ChairType]:
        if (
            (y, x) in visited
            or x < 0
            or x >= self.width
            or y < 0
            or y >= self.height
            or self.map[y][x] in self._WALL_CHARACTERS
        ):
            return
        visited.add((y, x))
        if self.map[y][x] in self._CHAIR_MARKERS:
            yield ChairType(self.map[y][x])
        yield from self._find_chairs_within_room(x - 1, y, visited)
        yield from self._find_chairs_within_room(x + 1, y, visited)
        yield from self._find_chairs_within_room(x, y - 1, visited)
        yield from self._find_chairs_within_room(x, y + 1, visited)

    def find_rooms_and_chairs(self) -> list[Room]:
        rooms: list[Room] = []
        room_markers = self._find_room_marker_positions()
        for room_name, (y, x) in room_markers:
            room = Room(name=room_name)
            for chair in self._find_chairs_within_room(x, y, visited=set()):
                room.chairs.append(chair)
            rooms.append(room)
        return rooms


def parse_floor_plan(floor_plan_ascii: str) -> Apartment:
    floor_plan = FloorPlan(floor_plan_ascii)
    rooms = floor_plan.find_rooms_and_chairs()
    return Apartment(rooms)
