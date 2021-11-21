import os
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv

load_dotenv()


class PostgresConnector:

    def __init__(self):
        self.connect = psycopg2.connect(database=os.getenv("PG_DB"),
                                        host=os.getenv("PG_HOST"),
                                        port=os.getenv("PG_PORT"),
                                        password=os.getenv("PG_PASSWORD"),
                                        user=os.getenv("PG_USER"))
        self.cursor = self.connect.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def get_data(self):
        self.cursor.execute("Select * from books")
        return self.cursor.fetchall()

    def insert_data(self, **kwargs):
        self.cursor.execute("""Insert into books (Author, Title, Publication_date, Language, Programming_Language)
                            VALUES (%s, %s, %s, %s, %s)
                            """, (kwargs['Author'], kwargs['Title'], kwargs['Publication_date'], kwargs['Language'],
                                  kwargs['Programming_language']))
        self.connect.commit()

    def edit_data(self, id_):
        self.cursor.execute('SELECT * FROM books WHERE id = %s', id_)
        data = self.cursor.fetchall()
        return data

    def update_data(self, id_, **kwargs):
        self.cursor.execute("""UPDATE books
                            SET Author= %s, Title= %s, Publication_date= %s, Language= %s, Programming_Language=%s
                            WHERE id = %s
                            """, (kwargs['Author'], kwargs['Title'], kwargs['Publication_date'], kwargs['Language'],
                                  kwargs['Programming_language'], id_))
        self.connect.commit()

    def delete_data(self, id_):
        self.cursor.execute("Delete from books where id = {0}".format(id_))
        self.connect.commit()
