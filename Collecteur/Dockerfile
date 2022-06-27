# syntax=docker/dockerfile:1
# Get the latest base image for python
FROM python:3.8.5-alpine
# Put files at the image '/app/' folder.
COPY . /app/
# '/app/' is base directory
WORKDIR /app/
# Expose port 9898 in the container
RUN pip3 install --upgrade pip
RUN pip3 install tqdm
#RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev
RUN pip3 install -r requirements.txt
#RUN --host='0.0.0.0'
# RUN --network=host
# execute the command
#CMD ["python3", "mainCollector.py", "run", "--host=0.0.0.0"]
CMD ["python3", "mainCollector.py"]


