import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ROUTES = {
    "src/cart.py": ["tests/test_cart.py"],
    "src/inventory.py": ["tests/test_inventory.py"],
    "src/pricing.py": ["tests/test_pricing.py"],
}

ALL_TESTS = ["tests"]


def select_tests(changed_files):
    selected = set()

    for file in changed_files:
        if file in ROUTES:
            selected.update(ROUTES[file])
        else:
            return ALL_TESTS

    return sorted(selected) if selected else ALL_TESTS


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--changed-files", nargs="*")
    args = parser.parse_args()

    if args.changed_files is None:
        parser.error("Please provide changed files")

    tests = select_tests(args.changed_files)

    print("Changed files:", args.changed_files)
    print("Selected tests:", tests)

    return subprocess.call(
        [sys.executable, "-m", "pytest", *tests],
        cwd=ROOT
    )


if __name__ == "__main__":
    raise SystemExit(main())
