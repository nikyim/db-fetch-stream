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
                SELECT TOP {} *
                FROM
                    {} (NOLOCK)
                WHERE
                    {} > {}
                ORDER BY
                    {} ASC
                """.format(table["size"],
                           table["name"],
                           table["primary_key"],
                           last_state["value"],
                           table["primary_key"]
                           )

        try:
            self.execute_query(query)
            fetch_rows = self.cur.fetchall()
            self.conn.commit()
            return fetch_rows

        except Exception as e:
            logger_helper.logger.error(e.args)
            return []
