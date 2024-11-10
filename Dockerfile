FROM python:3.12
LABEL MAINTAINER="Ryan | abolfazl.ryan@gmail.com"

ENV PYTHONUNBUFFERED 1

RUN mkdir /blogpy
WORKDIR /blogpy
COPY . /blogpy

ADD requirements.txt /blogpy
#RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "blogpy.wsgi:application"]
CMD ["python", "manage.py", "runserver"]
