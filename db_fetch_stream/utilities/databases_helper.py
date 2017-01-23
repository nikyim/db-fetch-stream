from settings.db import listing
import importlib


def get_db_list():
    result = []

    db_settings = listing.get_listing()
    for db in db_settings:
        db_config = importlib.import_module(db, package=None)
        result.append(db_config)

    return result
