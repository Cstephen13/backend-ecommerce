# Python and Linux Version
FROM python:3.8.3-alpine
RUN apk update \
    && apk add --virtual build-essential gcc python3-dev musl-dev libc-dev

COPY requirements.txt /app/requirements.txt
RUN pip install -U pip setuptools \
    && pip install wheel \
    && pip install --no-cache-dir -r /app/requirements.txt \
    && pip install gunicorn \
    && rm -rf /root/.cache \

# Configure server

#RUN set -ex \
#    && pip uninstall setuptools \
#    && pip install setuptools \
#    && pip install --upgrade pip \
#    && pip install --no-cache-dir -r /app/requirements.txt

# Working directory
WORKDIR /app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD . .

EXPOSE 8000

#CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "backend_e_commerce:application"]

CMD gunicorn --bind 0.0.0.0:8000 --pythonpath backend_e_commerce backend_e_commerce.config.wsgi:application