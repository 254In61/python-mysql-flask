"""
- Module to test mysql db connection.
- This will be part of the test suite/
"""


import mysql.connector
import os


# test independently
def query_db():
    connection = mysql.connector.connect(
            host=os.environ.get("MYSQL_SERVER_HOST"),
            user=os.environ.get("MYSQL_SERVER_USER"),
            password=os.environ.get("MYSQL_SERVER_PASSWD"),
            database=os.environ.get("MYSQL_DB_NAME")
    )

    if connection.is_connected():
        print("Connected to MySQL Server")
        cursor = connection.cursor(dictionary=True)
        # Sample query
        db_table = os.environ.get("MYSQL_DB_TABLE")
        cursor.execute(f"SELECT * FROM countries")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()
        connection.close()
        print("MySQL connection is closed")

if __name__ == "__main__":
    query_db()