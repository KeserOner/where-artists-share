FROM python:3.4

# Create app directory
RUN mkdir -p /usr/src/where-artists-share
WORKDIR /usr/src/where-artists-share

# Install requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["bash", "-e", "./serve.sh"]
