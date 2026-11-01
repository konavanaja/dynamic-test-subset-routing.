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

def select_tests(changed_files):
    selected = set()

    for file in changed_files:
        if file in ROUTES:
            selected.update(ROUTES[file])
        else:
            return ["tests"]

    return sorted(selected) if selected else ["tests"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", required=True)
    args = parser.parse_args()

    result = subprocess.run(
        ["git", "diff", "--name-only", args.base, args.head],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True
    )

    changed = result.stdout.splitlines()
    selected = select_tests(changed)

    print("Changed files:", changed)
    print("Selected tests:", selected)

    return subprocess.call(
        [sys.executable, "-m", "pytest", *selected,
         "--junitxml=test-results.xml"],
        cwd=ROOT
    )


if __name__ == "__main__":
    raise SystemExit(main())




