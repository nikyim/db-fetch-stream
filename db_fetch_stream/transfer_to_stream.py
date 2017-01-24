import importlib
from db_fetch_stream.utilities import last_state_helper


def commence(db_config):
    for table in db_config.TABLES:
        # Initialize db db_fetch class accordingly (transactions / differential)
        fetch_class = importlib.import_module("db_fetch_stream.db_fetch." + table["table_type"], package=None)
        fetch = fetch_class.FetchClass(db_config)

        # Get last state of the table
        last_state = last_state_helper.get_last_state(db_config.DB_CONFIG["db"] + "-" + table["name"])

        # Fetch records from db based on last state
        result = fetch.fetch(table, last_state)

        if len(result) == 0:
            pass
        else:
            for row in result:
                print(row[table["primary_key"]])

            # Assign last_state value variables
            last_result = result[-1]
            new_last_value = last_result[table["primary_key"]]
            if table["secondary_key"] != "":
                new_timestamp = last_result[table["secondary_key"]].strftime("%Y-%m-%d %H:%M:%S")
            else:
                new_timestamp = "Null"

            # Update last state value variables for each table respectively
            new_last_state = {
                "value": new_last_value,
                "last_timestamp": new_timestamp
            }
            last_state_helper.set_last_state(db_config.DB_CONFIG["db"] + "-" + table["name"], new_last_state)

    return None
