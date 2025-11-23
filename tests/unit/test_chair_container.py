import pytest

from floor_plan_parser.app.apartment import Apartment
from floor_plan_parser.domain import (
    ChairContainer,
    ChairType,
    ChairTypeCount,
    Room,
)


@pytest.mark.parametrize(
    ["chair_container", "expected_chair_types"],
    [
        (
            Room(
                "living room",
                [ChairType.PLASTIC, ChairType.WOODEN, ChairType.PLASTIC],
            ),
            {
                ChairType.WOODEN: 1,
                ChairType.PLASTIC: 2,
            },
        ),
        (
            Apartment(
                [
                    Room("one", [ChairType.WOODEN, ChairType.CHINA]),
                    Room("two", [ChairType.PLASTIC, ChairType.PLASTIC]),
                    Room("three", [ChairType.WOODEN, ChairType.SOFA]),
                ]
            ),
            {
                ChairType.WOODEN: 2,
                ChairType.PLASTIC: 2,
                ChairType.SOFA: 1,
                ChairType.CHINA: 1,
            },
        ),
    ],
)
def test_count_chair_types(
    chair_container: ChairContainer, expected_chair_types: ChairTypeCount
):
    # Given a room or an apartment containing chairs
    # When counting the types of chairs
    chair_types = chair_container.count_chair_types()

    # Then a mapping of chair type to number of chairs is returned
    assert chair_types == expected_chair_types
