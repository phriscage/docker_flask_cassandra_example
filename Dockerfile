################################################################################
##  Name:   Dockerfile
##  Date:   2015-11-29
##  Developer:  Chris Page
##  Email:  christophertpage@gmail.com
##  Purpose:   This Dockerfile contains the Docker builder commands for a simple
##	Flask application.
################################################################################
FROM python:3.5.0-slim

# Set the file maintainer (your name - the file's author)
MAINTAINER Chris Page

# install the python requirements
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt 

## run the app 
ADD app.py app.py

## expose the port
EXPOSE 5000

## start the command
CMD ["python", "app.py"]
