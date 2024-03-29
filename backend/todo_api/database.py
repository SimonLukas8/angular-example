import os
from pathlib import Path

from settings import SETTINGS
from tinydb import TinyDB

path = Path(os.path.realpath(SETTINGS.db_folder))
full_path = f"{path.absolute()}/database.json"

if not os.path.isdir(path.absolute()):
    raise Exception(f"Could not find db folder {path}")

if not os.path.isfile(full_path):
    open(full_path, 'a').close()

db = TinyDB(full_path)

USER_TABLE = db.table("user", cache_size=0)
TODO_TABLE = db.table("todo", cache_size=0)
