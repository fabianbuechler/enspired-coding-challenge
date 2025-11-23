import pathlib

import pytest

from floor_plan_parser.domain import ChairType


@pytest.fixture
def floor_plans_dir() -> pathlib.Path:
    return pathlib.Path(__file__).parent / "floor_plans"


@pytest.fixture
def floor_plan_ascii(floor_plans_dir: pathlib.Path, apartment_name: str) -> str:
    return (floor_plans_dir / f"{apartment_name}.txt").read_text()


@pytest.fixture
def expected_chairs_by_room(
    chairs_by_room: dict[str, str],
) -> dict[str, list[ChairType]]:
    return {
        room: sorted([ChairType(chair) for chair in chairs])
        for room, chairs in chairs_by_room.items()
    }
