import os
import shutil
import logging


logging.basicConfig(level=logging.INFO)


def main():
    copy_thing()


def copy_thing():
    source = "static"
    destination = "public"

    # It should first delete all the contents of the destination directory (public) to ensure that the copy is clean
    if os.path.exists(destination):
        logging.info(f"Removing existing directory: {destination}")
        shutil.rmtree(destination)

    # It should copy all files and subdirectories, nested files, etc.
    os.makedirs(destination, exist_ok=True)

    for name in os.listdir(source):
        src_path = os.path.join(source, name)
        dst_path = os.path.join(destination, name)

        if os.path.isdir(src_path):
            logging.info(f"Copying directory: {src_path} -> {dst_path}")
            shutil.copytree(src_path, dst_path)
        elif os.path.isfile(src_path):
            logging.info(f"Copying file: {src_path} -> {dst_path}")
            shutil.copy2(src_path, dst_path)
        else:
            logging.info(f"Skipping non-regular item: {src_path}")


if __name__ == "__main__":
    main()
