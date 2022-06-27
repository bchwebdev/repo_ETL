# syntax=docker/dockerfile:1
# Get the latest base image for python
FROM python:latest
# Put files at the image '/app/' folder.
COPY . /app/
WORKDIR /app/
RUN pip3 install --upgrade pip
RUN pip3 install tqdm
RUN pip3 install -r requirements.txt
#RUN --network=host
# '/app/' is base directory

# execute the command
CMD [ "python3", "appU1.py" ]