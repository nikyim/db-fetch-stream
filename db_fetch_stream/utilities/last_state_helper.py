from datetime import datetime
import json

from db_fetch_stream.utilities import logger_helper
from settings import common_settings


def get_last_state(table_name):

    try:
        last_state_file = open(common_settings.LAST_STATE_BASE_PATH + table_name + ".txt", 'r')

        return json.loads(last_state_file.read())
    except Exception as e:
        logger_helper.logger.info(e.args)
        logger_helper.logger.info("Creating last_state file...")
        set_initial_last_state(table_name)
        return get_last_state(table_name)


def set_last_state(table_name, state):
    last_state_object = json.dumps({"value": state["value"], "last_timestamp": state["last_timestamp"]})

    last_state_file = open(common_settings.LAST_STATE_BASE_PATH + table_name + ".txt", 'w')
    last_state_file.write(last_state_object)
    last_state_file.close()


def set_initial_last_state(table_name):
    last_state_object = json.dumps({"value": 1, "last_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

    last_state_file = open(common_settings.LAST_STATE_BASE_PATH + table_name + ".txt", 'w')
    last_state_file.write(last_state_object)
    last_state_file.close()
