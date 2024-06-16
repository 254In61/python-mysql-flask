Overview
========
- To build an application that queries country details
- A Python server that handles client requests and fetches data from a MySQL database.

Prerequisites
=============
- Python: Ensure Python is installed on your machine.
- MySQL: Ensure MySQL is installed and running.
- Python Packages: Install necessary Python packages.
- $ pip install flask mysql-connector-python

cicd
====
=> TDD approach applied
=> Test Driven Development(TDD) : Development and testing is reversed. 
   You write your unit tests first, and then implement code changes until the tests pass.
=> Jenkins used for CICD.
=> Pipeline name = jenkins-python-test-pipeline
=> Pipeline script is from SCM.
   - Jenkinsfile found in cicd/
=> Stages:
    1) clone repo  ** Not needed on the pipeline. Cloning down of Jenkinsfile achieves the stage.
    2) install dependencies 
    3) lint
    4) unittest
    5) integration test
    6) build
    7) ?? what next?
    


Design
=======
1. Git repo : https://github.com/254In61/python-mysql-flask.git
2. Flask Server:
- A simple Flask server is set up with a single endpoint /country that accepts GET requests.
- The server connects to a MySQL database using mysql-connector-python.
- When a request is received, the server queries the MySQL database for the country name provided in the request parameters.
  The result is returned as a JSON response.

3. Client:
- The client sends a GET request to the server with the country name as a parameter.
- The response from the server (country details) is printed.


Running the application
=======================
1. Start the Flask Server: $ python server.py
2. Run the Client: $ python client.py

