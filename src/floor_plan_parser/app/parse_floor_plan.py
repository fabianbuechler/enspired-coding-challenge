from typing import Self

from floor_plan_parser.domain import Apartment, Room


class FloorPlan:
    def __init__(self, floor_plan_ascii: str):
        self.ascii_lines = floor_plan_ascii.splitlines()
        width = max(len(line) for line in self.ascii_lines)
        self.map = np.genfromtxt(self.ascii_lines, dtype="U1", delimiter=[1] * width)
        self.height, self.width = self.map.shape


def parse_floor_plan(floor_plan_ascii: str) -> Apartment:
    floor_plan = FloorPlan(floor_plan_ascii)
    return None
