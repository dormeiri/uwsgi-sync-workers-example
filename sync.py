import sys
import time
import uuid
from pathlib import Path

__DATA_FILE = "data.txt"


def main():
    touch_reload_file = sys.argv[1]
    if not is_synced():
        sync()
        Path(touch_reload_file).touch()


def is_synced():
    origin_modified = (time.time() // 60) * 60  # Exclude seconds
    local_modified = Path(__DATA_FILE).stat().st_mtime
    return local_modified >= origin_modified


def sync():
    with open(__DATA_FILE, "w") as f:
        f.write(str(uuid.uuid4()))  # Write random data


def get_local_data():
    with open(__DATA_FILE, "r") as f:
        return f.read()


if __name__ == "__main__":
    main()
