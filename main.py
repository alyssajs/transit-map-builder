import sqlite3
from sqlite3 import Error
import pandas as pd


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_connection(r"C:\Users\rubbi\PycharmProjects\transit-project\db\pythonsqlite.db")
    conn = sqlite3.connect("pythonsqlite.db")
    data = pd.read_csv("pdb2022tr.csv")
    data.to_sql('users', conn, if_exists='append', index = False)


