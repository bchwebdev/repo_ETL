FROM python:3.8.5-alpine
COPY . /app
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip install flask
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["rest.py"]