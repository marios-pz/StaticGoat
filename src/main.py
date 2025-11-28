import os
import sys
import shutil
import logging
from page import generate_pages_recursive
from pathlib import Path

logging.basicConfig(level=logging.INFO)


def copy_directory_recursive(src: Path, dst: Path) -> None:
    if not dst.exists():
        dst.mkdir()

    for f in src.iterdir():
        new_f = dst / f.name
        if f.is_dir():
            copy_directory_recursive(f, new_f)
        else:
            print(f"Copying {f} to {new_f}")
            shutil.copy(f, new_f)


def main():
    if len(sys.argv) == 2:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    print(basepath)
    project_root = Path(__file__).parent.parent

    dest_path = project_root / "public"
    static_dir = project_root / "static"

    # remove before copying
    if dest_path.exists():
        shutil.rmtree(dest_path)

    copy_directory_recursive(static_dir, dest_path)

    from_path = project_root / "content"
    template_path = project_root / "template.html"

    generate_pages_recursive(from_path, template_path, dest_path, basepath)


if __name__ == "__main__":
    main()
