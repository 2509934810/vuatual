import pymysql
from utils.logs import logger
from utils.exceptions import DbConnection, SqlExecuteError


class Vmysql:
    def __init__(self, url, dbName, username, password):
        self.url = url
        self.dbName = dbName
        self.username = username
        self.password = password
        try:
            self.conn = pymysql.Connect(url, username, password, dbName)
        except Exception as e:
            logger.error("db connection error")
            raise DbConnection(
                "db connection error- {} - {} - {}".format(
                    self.url, self.username, self.password, self.dbName
                )
            )

    def executeSql(self, sql):
        data = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
        except Exception as e:
            logger.error("sql run error")
        finally:
            cursor.close()
            self.conn.close()
            return data
