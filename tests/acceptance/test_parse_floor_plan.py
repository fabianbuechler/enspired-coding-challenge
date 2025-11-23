import pytest

from floor_plan_parser.app.parse_floor_plan import parse_floor_plan
from floor_plan_parser.domain import ChairType


@pytest.mark.parametrize(
    ["apartment_name", "expected_room_names"],
    [
        (
            "apartment_a",
            {
                "balcony",
                "bathroom",
                "closet",
                "kitchen",
                "living_room",
                "office",
                "sleeping room",
                "toilet",
            },
        ),
    ],
)
def test_identifies_rooms(floor_plan_ascii: str, expected_room_names: set[str]):
    # Given an ASCII floor plan of an apartment
    # When parsing that floor plan
    apartment = parse_floor_plan(floor_plan_ascii)

    # The rooms of the apartment are identified
    room_names = {room.name for room in apartment.rooms}
    assert room_names == expected_room_names


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
                "living_room": "SSWWWWWW",
                "office": "PWW",
                "sleeping room": "SW",
                "toilet": "C",
            },
        ),
    ],
)
def test_locates_chairs_within_rooms(
    floor_plan_ascii: str, expected_chairs_by_room: dict[str, list[ChairType]]
):
    # Given an ASCII floor plan
    # When parsing that floor plan
    apartment = parse_floor_plan(floor_plan_ascii)

    # And different types of chairs located in the rooms
    chairs_by_room = {room.name: sorted(room.chairs) for room in apartment.rooms}
    assert chairs_by_room == expected_chairs_by_room
