FROM python:3.7-alpine

RUN apk --upgrade add --no-cache \
        bash \
        gcc \
        musl-dev \
#        linux-headers \
        libffi-dev \
       	libxml2-dev \
        libxslt-dev \
        openssl-dev

ADD requirements.txt /opt/
RUN pip install --upgrade --no-cache-dir -r /opt/requirements.txt

COPY archiver/ /archiver

ADD .env /
ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
