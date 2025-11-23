import operator

from floor_plan_parser.app import Apartment
from floor_plan_parser.domain import ChairType, ChairTypeCount


class LegacySystemApartmentPresener:
    """Format chair type counts for apartment and all rooms.

    List apartment as "total" followed by rooms sorted alphabetically.

    """

    _chair_type_order = [
        ChairType.WOODEN,
        ChairType.PLASTIC,
        ChairType.SOFA,
        ChairType.CHINA,
    ]

    def _format_chair_counts(self, chair_types: ChairTypeCount) -> str:
        return ", ".join(
            [
                f"{chair_type.value}: {chair_types.get(chair_type, 0)}"
                for chair_type in self._chair_type_order
            ]
        )

    def __call__(self, apartment: Apartment) -> str:
        lines: list[str] = [
            "total:",
            self._format_chair_counts(apartment.count_chair_types()),
        ]
        for room in sorted(apartment.rooms, key=operator.attrgetter("name")):
            lines.extend(
                [
                    f"{room.name}:",
                    self._format_chair_counts(room.count_chair_types()),
                ]
            )
        return "\n".join(lines)
