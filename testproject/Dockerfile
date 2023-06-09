FROM python:3.8

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /test
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

#CMD ['python','manage.py','runserver']

#ENTRYPOINT ["top", "-b"]