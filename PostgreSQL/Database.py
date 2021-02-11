import psycopg2 as psql

class Database:

    def __init__(self, conf):

        try:

            self.__host = conf['host']
            self.__name = conf['name']
            self.__user = conf['user']
            self.__pass = conf['pass']
            self.__port = conf['port']
            self.__conn = None
            self.connect()

        except Exception as e:

            print('Error: setup fail ({})'.format(str(e)))

    def connect(self):

        try:

            self.__conn = psql.connect(database=self.__name, user=self.__user, password=self.__pass, host=self.__host, port=self.__port)

        except Exception as e:

            print('Error: connection fail ({})'.format(str(e)))


    def getall(self, table, fields, where=None):

        try:

            sql = "SELECT {} FROM {}{};"

            where = "" if where is None else " WHERE {}".format(where)
            sql_query = sql.format(','.join(fields), table, where)
            cur = self.__conn.cursor()
            cur.execute(sql_query)
            rows = cur.fetchall()
            self.__conn.commit()
            self.__conn.close()
            return rows

        except Exception as e:

            print('Error: connection fail ({})'.format(str(e)))
