import textwrap

from floor_plan_parser.adapters.presenters import LegacySystemApartmentPresener
from floor_plan_parser.app import Apartment
from floor_plan_parser.domain import ChairType, Room


def test_legacy_system_apartment_presenter_format():
    # Given an apartment with rooms and chairs
    apartment = Apartment(
        rooms=[
            Room("living room", [ChairType.WOODEN, ChairType.WOODEN, ChairType.SOFA]),
            Room("kitchen", [ChairType.PLASTIC, ChairType.PLASTIC]),
            Room("office", [ChairType.CHINA, ChairType.SOFA]),
        ]
    )

    # When formatting that for presentation to the legacy system
    presenter = LegacySystemApartmentPresener()
    result = presenter(apartment)

    # Then the result is formatted according to the legacy system specs
    assert result == textwrap.dedent(
        """\
        total:
        W: 2, P: 2, S: 2, C: 1
        kitchen:
        W: 0, P: 2, S: 0, C: 0
        living room:
        W: 2, P: 0, S: 1, C: 0
        office:
        W: 0, P: 0, S: 1, C: 1"""
    )
