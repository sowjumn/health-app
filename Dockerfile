#Grab the latest alpine image
#FROM alpine:latest
FROM heroku/heroku:16

# ALPINE Install python and pip
#RUN apk add --update python-dev py-pip bash postgresql-dev gcc musl-dev curl openssh 

# Heroku-16 Install python and pip
RUN apt-get update && apt-get install -y python3-pip


ADD requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip3 install -r /tmp/requirements.txt

# Add our code
ADD . /opt/webapp/
WORKDIR /opt/webapp

ADD /.profile.d /app/.profile.d 

# ALPINE Run the image as a non-root user
#RUN adduser -D myuser

# Heroku-16 Run the image as a non-root user
RUN useradd -m myuser

USER myuser


# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku			

EXPOSE 5000
CMD gunicorn --bind 0.0.0.0:$PORT wsgi --reload
#CMD python app.py
