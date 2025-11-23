import operator

import pytest

from floor_plan_parser.app.parse_floor_plan import FloorPlan
from floor_plan_parser.domain import ChairType


@pytest.mark.parametrize(
    ["apartment_name", "chairs_by_room"],
    [
        (
            "apartment_a",
            {
                "balcony": "PP",
                "bathroom": "P",
                "closet": "PPP",
                "kitchen": "WWWW",
                "living room": "SSWWWWWWW",
                "office": "PWW",
                "sleeping room": "SW",
                "toilet": "C",
            },
        ),
        (
            "apartment_b",
            {
                "bedroom": "W",
                "closet": "CPP",
                "sleeping room": "SW",
                "toilet": "C",
            },
        ),
    ],
)
def test_floor_plan_find_rooms_and_chairs(
    floor_plan_ascii: str, expected_chairs_by_room: dict[str, list[ChairType]]
):
    # Given an ASCII floor plan
    floor_plan = FloorPlan(floor_plan_ascii)

    # When parsing that floor plan
    rooms = floor_plan.find_rooms_and_chairs()

    # Then the rooms are identified by their markers
    # And different types of chairs are located in the rooms
    chairs_by_room = {
        room.name: sorted(room.chairs, key=operator.attrgetter("value"))
        for room in rooms
    }
    assert chairs_by_room == expected_chairs_by_room
