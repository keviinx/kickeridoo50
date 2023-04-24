FROM python:3.10-slim

WORKDIR /usr/src/app

EXPOSE 5000

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=application.py

CMD ["flask", "run", "--host=0.0.0.0"]
