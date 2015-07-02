############################################################
# Dockerfile to build was container images
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM ubuntu:14.04

MAINTAINER WorstCorp

# Update the repository sources list
RUN apt-get update -y

################## BEGIN INSTALLATION ######################
# Install Python
RUN apt-get install -y python-pip python-dev build-essential && pip install --upgrade pip

# Install Git
RUN apt-get install -y git

# Clone Git Repo
RUN cd /
RUN git clone https://github.com/KeserOner/where-artists-share

# Install requirements
RUN pip install -r /where-artists-share/requirements.txt