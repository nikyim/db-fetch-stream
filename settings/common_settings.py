# coding: utf-8

from logging import DEBUG

APP_NAME = "db_fetch_stream"

LOG_DIR = "/var/db-fetch-stream/log/"
LOG_FILE_NAME = "db_fetch_stream.log"
LOG_LEVEL = DEBUG

LAST_STATE_BASE_PATH = "/var/db-fetch-stream/last-state/"

AWS_KINESIS_CONFIG = {
    "access_key": "",
    "secret_key": "",
    "stream": ""
}