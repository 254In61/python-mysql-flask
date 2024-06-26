"""
- Server module
- Server receives a query from client.
- Server queries the mysql db server in the backend
"""

import os
import mysql.connector
from mysql.connector import Error
from flask import Flask, jsonify

app = Flask(__name__)
# An instance of Flask constructor.
# takes the name of current module (__name__) as argument.


def db_details():
    """
    - Function to collect mysql login details.
    - Could be changed
    """
    host_ip = os.environ.get("MYSQL_SERVER_HOST")
    db_user = os.environ.get("MYSQL_SERVER_USER")
    db_pswd = os.environ.get("MYSQL_SERVER_PASSWD")
    db_name = os.environ.get("MYSQL_DB_NAME")

    return host_ip, db_user, db_pswd, db_name


def mysql_query(query):
    """
    - Function that performs the mysql query.
    - Returns results as raw back to the calling method.
    """
    host_ip, db_user, db_pswd, db_name = db_details()
    try:
        connection = mysql.connector.connect(
            host=host_ip, user=db_user, password=db_pswd, database=db_name
        )

        if connection.is_connected():
            print("Connected to MySQL Server")
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query)

            if query == "SELECT * FROM countries":
                result = cursor.fetchall()

            else:
                result = cursor.fetchone()

            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return result

    except Error as error_generated:
        print("Error while connecting to MySQL", error_generated)
        return error_generated


# The route() function of the Flask class is a decorator.
# decorator tells the application which URL should call the associated function.


@app.route("/country/<name>", methods=["GET"])
def get_country(name):
    """
    - GET method.
    - Function reads data and sends back as json ouptut
    """
    # name = request.args.get('name')

    if name == "all":
        query = "SELECT * FROM countries"

    else:
        query = f"SELECT * FROM countries where country = '{name}'"

    print(f"Query : {query}")

    result = mysql_query(query)
    print(result)
    return jsonify(result)  # Even if no data, it will empty data?

    # if result:
    #     return jsonify(result)
    #     # return result
    # else:
    #     return jsonify({"error": "Country not found"}), 404
    #     # return "error : Country not found"


# def put_country():
#     """
#     - PUT method
#     """
#     pass


# def post_country():
#     """
#     - POST method
#     """
#     pass


# def delete_country():
#     """
#     - DELETE method
#     """


if __name__ == "__main__":
    app.run(debug=True)
