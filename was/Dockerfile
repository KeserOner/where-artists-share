############################################################
# Dockerfile to build WAS container
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM python:3.4

################## BEGIN INSTALLATION ######################
# Create the working directory
RUN mkdir /where-artists-share
WORKDIR /where-artists-share

# Install all the requirements & Migrate
ADD * ./
RUN pip install -r requirements.txt
RUN python manage.py migrate

# Exposing port 8000
EXPOSE 8000