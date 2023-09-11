import sqlite3 as sq
import os

connection = None
cursor = None

data_name = "Assets/Databases/Data.db"

data = os.path.abspath(data_name)


def open_db(name):
    global connection, cursor
    connection = sq.connect(name)
    cursor = connection.cursor()


def close():
    global connection, cursor
    connection.close()


def create():
    global data
    open_db(data)
    cursor.execute("CREATE TABLE IF NOT EXISTS control (id INTEGER PRIMARY KEY,key TEXT,value INTEGER)")
    connection.commit()
    close()


def delete(db_name, table):
    open_db(db_name)
    cursor.execute(f"DROP TABLE {table}")
    connection.commit()
    close()


def enter(db_name, array, table, col):
    open_db(db_name)
    columns = '?'
    for i in range(col):
        columns += ', ?'

    cursor.executemany(f'''INSERT INTO {table} VALUES (Null, {columns});''', [array])
    connection.commit()
    close()


def get_data(db_name, table):
    open_db(db_name)
    cursor.execute(f"SELECT * FROM {table}")
    data = cursor.fetchall()
    close()
    return data


def delete_value(id, db_name, table):
    open_db(db_name)
    cursor.execute(f"DELETE FROM {table} WHERE id = {id}")
    connection.commit()
    close()


def delete_all():
    delete(data, "control")


def sql_call_where(db_name, table, requirement):
    open_db(db_name)
    cursor.execute(f"SELECT id FROM {table} WHERE login = '{requirement}'")
    end = cursor.fetchone()
    close()
    return end


def get_image_with_name(db_name, table, requirement):
    open_db(db_name)
    cursor.execute(f"SELECT avatar FROM {table} WHERE name = '{requirement}'")
    end = cursor.fetchone()
    close()
    return end


def update_db(db_name, col, table, value, id):
    open_db(db_name)
    cursor.execute(f"UPDATE {table} SET {col} = ? WHERE id = {id}", [(value)])
    connection.commit()
    close()