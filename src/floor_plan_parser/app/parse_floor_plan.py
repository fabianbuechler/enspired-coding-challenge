import operator
import re
from collections.abc import Iterable

from floor_plan_parser.domain import Apartment, Room

type Coordinate = tuple[int, int]


class FloorPlan:
    _re_room_marker: re.Pattern = re.compile(r"\((?P<name>[\w\s]+)\)", re.ASCII)

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


def parse_floor_plan(floor_plan_ascii: str) -> Apartment:
    floor_plan = FloorPlan(floor_plan_ascii)
    return None
