"""
- Server module
- Server receives a query from client.
- Based on type of request received from client, server queries the mysql db server in the backend
"""
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# MySQL database connection
# db = mysql.connector.connect(
#     host="localhost",
#     user="yourusername",
#     password="yourpassword",
#     database="country_db"
# )
def db_details():
    """
    Function to collect details.
    As of now, the credentials and other details are read as environmental variables.
    This could be changed to have credentials from Secrets Manager like Hashicorp Vault
    """
    host_ip = os.environ.get("MYSQL_SERVER_HOST")
    db_user = os.environ.get("MYSQL_SERVER_USER")
    db_pswd = os.environ.get("MYSQL_SERVER_PASSWD")
    db_name = os.environ.get("MYSQL_DB_NAME")

    return host_ip,db_user,db_pswd,db_name


@app.route('/country', methods=['GET'])
def get_country():
    name = request.args.get('name')
    query = f"SELECT * FROM countries WHERE name = {name}"

    host_ip, db_user, db_pswd, db_name = db_details()
    try:
        connection = mysql.connector.connect(
            host=host_ip,
            user=db_user,
            password=db_pswd,
            database=db_name
        )

        if connection.is_connected():
            print("Connected to MySQL Server")
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query)
            result = cursor.fetchone()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

            if result:
                return jsonify(result)
            else:
                return jsonify({"error": "Country not found"}), 404

    except Error as e:
        print("Error while connecting to MySQL", e)
        return e, False

if __name__ == '__main__':
    app.run(debug=True)