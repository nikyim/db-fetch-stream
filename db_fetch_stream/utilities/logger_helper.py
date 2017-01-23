from logging import getLogger, Formatter
from logging.handlers import RotatingFileHandler

from settings import common_settings

logger = getLogger()

handler = RotatingFileHandler(
    common_settings.LOG_DIR + common_settings.LOG_FILE_NAME,
    maxBytes=10000, backupCount=1
)

formatter = Formatter(
    "%(asctime)s %(levelname)s: %(message)s "
    "[in %(pathname)s:%(lineno)d]"
)

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(common_settings.LOG_LEVEL)
