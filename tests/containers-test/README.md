Overview
=========
- Docker containers testing is done here.
- Idea is to use Docker containers as clients to test the code.

Design
======
- A docker image is built using Dockerfile. It is an Ubuntu image running python.
- Ansible is installed on your environment, if it wasn't there.
- Bash script, run-docker-testing.sh does all that for you.

How To Use
==========
- Run $ ./run-docker-testing.sh

Assumptions:
   - Your server side is running OK and your mysql is OK.
   - Ansible is installed in your environment

Tshoot
=======
=> Check containers content : $ docker exec <container_name> ls -l
