from psycopg2 import pool

## defining connect method once helps with code repetetion

# def connect():
#     return psycopg2.connect(user="postgres", password="1234", database="learn", host="localhost")

## creating a pool of connections keeps them open and available to be requested from the code

# __connection_pool = pool.SimpleConnectionPool(1,
#                                             10,
#                                             user="postgres",
#                                             password="1234",
#                                             database="learn",
#                                             host="localhost" )


# class ConnectionPool:
#     def __init__(self):
#         self.__connection_pool = pool.SimpleConnectionPool(1,
#                                                          10,
#                                                          user="postgres",
#                                                          password="1234",
#                                                          database="learn",
#                                                          host="localhost" )
#
#
#     def __enter__(self):
#         return self.__connection_pool.getconn()
#
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.__connection_pool.putconn() # return the connection
#         pass

class Database:
    __connection_pool = None

    @classmethod
    def initialise(cls, **kwargs):
        cls.__connection_pool = pool.SimpleConnectionPool(1, 10, **kwargs)

    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        Database.__connection_pool.putconn(connection)

    @classmethod
    def close_all_connections(cls):
        Database.__connection_pool.closeall()


class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None
        return self.cursor


    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.connection


    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value is not None: # There was an error
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.return_connection(self.connection)
