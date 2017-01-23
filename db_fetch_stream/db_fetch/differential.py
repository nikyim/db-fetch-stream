from db_fetch_stream.connector.db_connector import DBConnector
from db_fetch_stream.utilities import logger_helper


class FetchClass(DBConnector):
    def fetch(self, table, last_state):

        query = ""

        if self.db_config.DB_CONFIG["type"] == "mysql":
            query = """
            SELECT *
            FROM
                {}
            WHERE
                {} > {}
            ORDER BY
                {} ASC
            LIMIT {}
            """.format(table["name"],
                       table["primary_key"],
                       last_state["value"],
                       table["primary_key"],
                       table["size"])

        elif self.db_config.DB_CONFIG["type"] == "mssql":
            query = """
                SELECT *
                FROM
                    {} (NOLOCK)
                WHERE
                    {} > {}
                ORDER BY
                    {} ASC
                LIMIT {}
                """.format(table["name"],
                           table["primary_key"],
                           last_state["value"],
                           table["primary_key"],
                           table["size"])

        try:
            self.execute_query(query)
            self.conn.commit()

            return self.cur.fetchall()
        except Exception as e:
            logger_helper.logger.error(e.args)
            return []
