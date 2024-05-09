FROM python:3.12.3
WORKDIR /app

ADD . /app
COPY . /app
RUN pip install -r requirements.txt
#RUN apt-get update && apt-get install -y netcat-openbsd
#COPY wait-for-postgres.sh /app/wait-for-postgres.sh
#RUN chmod +x /app/wait-for-postgres.sh
#RUN apt-get update && apt-get install -y postgresql-client
CMD ["python", "Task_1.py"]

