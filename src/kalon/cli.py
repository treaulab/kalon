"""Command-line entry point."""

from importlib.metadata import version


def main() -> None:
    """Print the installed version."""
    print(f"kalon {version('kalon')}")
