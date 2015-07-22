############################################################
# Dockerfile to build WAS container
# Based on Python
############################################################

# Set the base image to Python
FROM python:3.4

################## BEGIN INSTALLATION ######################
# Install all requirements
ADD requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

# Create the working directory
RUN mkdir /where-artists-share
WORKDIR /where-artists-share

# Migrate
#ADD * ./

# Exposing port 8000
EXPOSE 8000

CMD ["bash", "-e", "./setup.sh"]