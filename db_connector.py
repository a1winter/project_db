import mysql.connector

class DatabaseConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        self.connection = None
        self.cursor = None


    def connect(self):  # подключение к БД
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database)

        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):  # передает запрос к БД
        if self.cursor is None:
            raise ConnectionError('Соединение не установлено. Вызовите метод connect()')

        self.cursor.execute(query, params or [])
        self.connection.commit()
        return self.cursor.fetchall()

    def close(self):  # закрытие соединения с БД
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

