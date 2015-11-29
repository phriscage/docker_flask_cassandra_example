# docker_flask_cassandra_example
================================
    
A sample Python Flask application using Cassandra and Docker containers.
*Using the **default** docker machine name for non-swarm deployment*

## Quick Start
-------------------------

* Docker Compose:

	`docker-compose up`

* Verify:

	`curl -X GET -s -D - http://$(docker-machine ip default):8000/test`

## Development Configuration:
-------------------------

* Cassandra Docker container:

	`docker run -d --name flask_cassandra -p 9042:9042 -t cassandra:2.2.0`

* Python Virtualenv:

   	`mkvirtualenv docker_flask_cassandra_example -r requirements.txt`

* Python Flask application:

	`CASSANDRA_PORT_9042_TCP_ADDR=$(docker-machine ip default) CASSANDRA_PORT_9042_TCP_PORT=9042 python app.py`

