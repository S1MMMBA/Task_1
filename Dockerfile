FROM python:3.12.3
WORKDIR /app
ADD . /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "Task_1.py"]