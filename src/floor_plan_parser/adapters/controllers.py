import pathlib

from floor_plan_parser.app.parse_floor_plan import (
    ApartmentPresenterProtocol,
    parse_floor_plan,
)


class ParseFloorPlanController:
    """Controller for the parse floor-plan use-case."""

    def __init__(self, presenter: ApartmentPresenterProtocol):
        self.presenter = presenter

    def parse_floor_plan(self, floor_plan_file: pathlib.Path) -> str:
        floor_plan_ascii = floor_plan_file.read_text()
        apartment_chair_plan = parse_floor_plan(
            floor_plan_ascii=floor_plan_ascii,
            apartment_presenter=self.presenter,
        )
        return apartment_chair_plan
