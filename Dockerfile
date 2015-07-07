############################################################
# Dockerfile to build WAS container
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM ubuntu:14.04

################## BEGIN INSTALLATION ######################
RUN apt-get update

# Install Python & PIP
RUN apt-get install -y \
python-pip \
python-dev \
build-essential

# Update PIP
RUN pip install --upgrade pip

# Create the working directory
RUN mkdir /where-artists-share
WORKDIR /where-artists-share

# Install all the requirements
ADD requirements.txt /where-artists-share/
RUN pip install -r requirements.txt

# Copying all the files to the projet folder on the docker image
ADD . /where-artists-share

# Exposing port 8000
EXPOSE 8000