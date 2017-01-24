import pymysql
import pymssql

from db_fetch_stream.utilities import logger_helper


class DBConnector(object):
    def __init__(self, db_config):
        self.db_config = db_config

        try:
            if db_config.DB_CONFIG["type"] == "mysql":
                self.conn = pymysql.connect(host=db_config.DB_CONFIG["host"],
                                            port=db_config.DB_CONFIG["port"],
                                            user=db_config.DB_CONFIG["username"],
                                            passwd=db_config.DB_CONFIG["password"],
                                            db=db_config.DB_CONFIG["dbname"],
                                            cursorclass=pymysql.cursors.DictCursor)

                self.cur = self.conn.cursor()

            elif db_config.DB_CONFIG["type"] == "mssql":
                self.conn = pymssql.connect(server=db_config.DB_CONFIG["host"],
                                            user=db_config.DB_CONFIG["username"],
                                            password=db_config.DB_CONFIG["password"],
                                            database=db_config.DB_CONFIG["dbname"],
                                            as_dict=True)

                self.cur = self.conn.cursor()
        except Exception as e:
            logger_helper.logger.error(e.args)

    def execute_query(self, query):
        try:
            self.cur.execute(query)

        except Exception as e:
            logger_helper.logger.error(e.args)
            logger_helper.logger.error(
                "Execute query failed with the db connector, please check"
            )

