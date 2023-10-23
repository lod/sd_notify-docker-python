FROM docker.io/library/python:3.10-slim-bullseye

COPY test.py /

RUN pip install sdnotify
RUN chmod 755 /test.py

ENTRYPOINT ["/usr/local/bin/python", "test.py"]
