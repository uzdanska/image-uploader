FROM python:3.10.10

ENV PYTHONDOCKER=1

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

# EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]