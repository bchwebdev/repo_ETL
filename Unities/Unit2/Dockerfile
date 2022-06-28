# syntax=docker/dockerfile:1
# Get the latest base image for python
FROM python:latest
# Put files at the image '/app/' folder.
COPY . /app

RUN apt-get update
RUN apt-get -y upgrade
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
# RUN --network=host

# '/app/' is base directory
WORKDIR /app/
# execute the command
CMD [ "python3", "appU2.py" ]