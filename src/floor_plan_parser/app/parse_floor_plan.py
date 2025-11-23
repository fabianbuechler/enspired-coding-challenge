from typing import Self

from floor_plan_parser.domain import Apartment, Room


class FloorPlan:
    def __init__(self, floor_plan_ascii: str):
        self.ascii = floor_plan_ascii


def parse_floor_plan(floor_plan_ascii: str) -> Apartment:
    floor_plan = FloorPlan(floor_plan_ascii)
    return None
