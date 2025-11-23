import operator
import textwrap

import numpy as np
import pytest

from floor_plan_parser.app.parse_floor_plan import Coordinate, FloorPlan


@pytest.mark.parametrize(
    ["floor_plan_ascii", "ascii_2d_array"],
    [
        (
            textwrap.dedent(
                """\
                abc
                de
                fghi
                """
            ),
            np.array(
                [
                    ["a", "b", "c", ""],
                    ["d", "e", "", ""],
                    ["f", "g", "h", "i"],
                ],
                dtype="<U1",
            ),
        )
    ],
)
def test_floor_plan_loads_ascii_plan_as_2d_array_map(
    floor_plan_ascii: str, ascii_2d_array: np.typing.ArrayLike
):
    # Given an ASCII floor plan of an apartment
    # When initializing a FloorPlan
    floor_plan = FloorPlan(floor_plan_ascii)

    # Then the floor plan is loaded into a 2d char array map
    assert np.array_equal(floor_plan.map, ascii_2d_array)
    assert floor_plan.width == 4
    assert floor_plan.height == 3


@pytest.mark.parametrize(
    ["floor_plan_ascii", "expected_room_marker_positions"],
    [
        (
            textwrap.dedent(
                """\
                |  (closet)   +-----------------+------------+
                +-------------+  (living room)  | (kitchen)  |
                """
            ),
            [
                ("closet", (0, 7)),
                ("living room", (1, 23)),
                ("kitchen", (1, 38)),
            ],
        )
    ],
)
def test_find_room_marker_positions(
    floor_plan: FloorPlan, expected_room_marker_positions: list[tuple[str, Coordinate]]
):
    # Given an ASCII floor plan
    # When finding room marker positions
    room_markers = floor_plan._find_room_marker_positions()

    # Then room markers' positions are detected
    sort_by_coordinate = operator.itemgetter(1)
    assert (
        sorted(room_markers, key=sort_by_coordinate) == expected_room_marker_positions
    )
