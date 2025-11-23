import pathlib
import subprocess


def test_floor_plan_parser_cli(floor_plans_dir: pathlib.Path):
    # Given a floor plan file
    floor_plan_file = floor_plans_dir / "apartment_b.txt"

    # When running the floor-plan-parser CLI
    output = subprocess.getoutput(f"floor-plan-parser {floor_plan_file}")

    # The CLI invokes parses the floor-plan and prints the appartment chair plan
    assert output.startswith("total:")
