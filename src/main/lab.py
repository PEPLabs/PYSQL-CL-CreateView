import os
import sqlite3

"""
SQL sublanguage: DDL (Data Definition Language)

A VIEW in SQL is a virtual table that was created based on a SQL statement that was predefined.

The syntax for creating a view is as follows:
CREATE VIEW view_name AS sql_statement;
"""

_LAB_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _read_sql(filename):
    with open(os.path.join(_LAB_DIR, filename), "r", encoding="utf-8") as f:
        return f.read().strip()


def problem1():
    """
    site_user table:
    |   id  |     firstname        |        lastname        |   age   |
    -------------------------------------------------------------------
    |1      |'Steve'               |'Garcia'                |23       |
    |2      |'Alexa'               |'Smith'                 |40       |
    |3      |'Steve'               |'Jones'                 |29       |
    |4      |'Brandon'             |'Smith'                 |50       |
    |5      |'Adam'                |'Jones'                 |61       |

    problem1: Create a view called "firstname_lastname" in problem1.sql from the site_user table that only has
    the firstname and lastname columns.

    NOTE: This table should NOT have the id and age.

    Sets up the site_user table, runs the student's CREATE VIEW statement, and returns the open connection so
    the caller can verify the view's contents.
    """
    sql = _read_sql("problem1.sql")

    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE site_user (id INTEGER PRIMARY KEY AUTOINCREMENT, firstname varchar(100), "
        "lastname varchar(100), age int);"
    )
    cur.execute("INSERT INTO site_user (firstname, lastname, age) VALUES ('Steve', 'Garcia', 23);")
    cur.execute("INSERT INTO site_user (firstname, lastname, age) VALUES ('Alexa', 'Smith', 40);")
    cur.execute("INSERT INTO site_user (firstname, lastname, age) VALUES ('Steve', 'Jones', 29);")
    cur.execute("INSERT INTO site_user (firstname, lastname, age) VALUES ('Brandon', 'Smith', 50);")
    cur.execute("INSERT INTO site_user (firstname, lastname, age) VALUES ('Adam', 'Jones', 61);")
    conn.commit()

    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print(f"problem1: {e}\n")

    return conn
