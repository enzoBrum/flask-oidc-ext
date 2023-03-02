#!/usr/bin/env python3
import subprocess

__VERSION__ = "1.4.5"

def bump_patch_number(version_number: str) -> str:
    """Return a copy of `version_number` with the patch number incremented."""
    major, minor, patch = version_number.split(".")
    return f"{major}.{minor}.{int(patch) + 1}"


def create_new_patch_release():
    """Create a new patch release on GitHub."""
    # new_version_number = bump_patch_number(last_version_number)

    subprocess.run(
        ["gh", "release", "create", "--generate-notes", __VERSION__],
        check=True,
    )


if __name__ == "__main__":
    create_new_patch_release()
