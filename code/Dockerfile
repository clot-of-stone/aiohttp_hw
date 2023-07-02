FROM python:3.10-alpine3.17

WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

# RUN python app/main.py
