# Dockerfile

FROM python:3.10.1-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip

CMD python -m venv .venv

COPY .venv/Scripts/activate /app/

CMD . /app/.venv/Scripts/activate

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt
COPY . /app/

CMD ["python", "-m", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]




