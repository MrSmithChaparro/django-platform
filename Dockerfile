FROM python:3.10.12

WORKDIR /app
COPY requirements.txt /app/

RUN apt-get update -y
RUN apt-get install -y pkg-config libmariadb-dev-compat libmariadb-dev build-essential python3-dev

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]