import pathlib

from floor_plan_parser.adapters.controllers import ParseFloorPlanController
from floor_plan_parser.app import Apartment


def dummy_apartment_presenter(apartment: Apartment) -> str:
    return ", ".join(room.name for room in apartment.rooms)


def test_parse_floor_plan_controller(floor_plans_dir: pathlib.Path):
    controller = ParseFloorPlanController(presenter=dummy_apartment_presenter)
    apartment_chair_plan = controller.parse_floor_plan(
        floor_plan_file=floor_plans_dir / "apartment_b.txt"
    )
    assert apartment_chair_plan == "bedroom, toilet, closet, sleeping room"
