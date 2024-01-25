FROM python:3.11-alpine
WORKDIR /usr/src/

# env variables
ENV HOST=0.0.0.0

# upgrade pip
RUN pip install --upgrade pip

# install dependencies
COPY requirements.txt /usr/src/
RUN pip install -r requirements.txt

# create rootless group/user
RUN addgroup --system python && adduser \
    -S -H -s /usr/sbin/nologin -G python python

COPY --chown=python:python app.py /usr/src/
COPY --chown=python:python app/ /usr/src/app/

USER python

ENTRYPOINT ["python", "app.py"]
