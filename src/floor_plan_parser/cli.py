import argparse
import pathlib
import textwrap

from floor_plan_parser.adapters.controllers import ParseFloorPlanController
from floor_plan_parser.adapters.presenters import LegacySystemApartmentPresener


def _make_argument_parser() -> argparse.ArgumentParser:
    argument_parser = argparse.ArgumentParser(
        description=textwrap.dedent(
            """\
            Floor Plan Parser

            Parse ASCII floor-plan files and print chair type counts
            for the apartment (totals) and for all rooms.

            Chair types: W (wooden), P (plastic), S (sofa), C (china)
            """
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    argument_parser.add_argument(
        "floor_plan_file", type=pathlib.Path, help="Path to floor-plan file"
    )
    return argument_parser


def floor_plan_parser():
    """CLI entrypoint for floor-plan-parser."""
    argument_parser = _make_argument_parser()
    args = argument_parser.parse_args()

    # Ensure floor-plan file exists
    floor_plan_file = args.floor_plan_file
    if not floor_plan_file.exists():
        argument_parser.error(f"floor_plan_file doesn't exist at {floor_plan_file!s}")

    # Initialize controller, presenter and run use-case
    presenter = LegacySystemApartmentPresener()
    parse_floor_plan_controller = ParseFloorPlanController(presenter)
    apartment_chair_plan = parse_floor_plan_controller.parse_floor_plan(floor_plan_file)

    # Print formatted apartment chair plan
    print(apartment_chair_plan)
