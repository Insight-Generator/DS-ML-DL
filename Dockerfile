FROM python:3.8.2-slim
ENV PYTHONUNBUFFERED 1

#RUN apt-get update && \
#    apt-get install -y \
#      gcc \
#      libpq-dev

COPY requirements.txt /opt/celery/
RUN pip install -r /opt/celery/requirements.txt

RUN groupadd -r celery && useradd --no-log-init -r -g celery celery -m

COPY --chown=celery:celery correlation_analysis.py /opt/celery/
COPY --chown=celery:celery IceCreamData.csv /opt/celery/

WORKDIR /opt/celery/