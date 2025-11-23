import numpy as np
import pytest
import textwrap

from floor_plan_parser.app.parse_floor_plan import FloorPlan


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
