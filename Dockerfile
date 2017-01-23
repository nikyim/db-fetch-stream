FROM continuumio/anaconda3
MAINTAINER Kheng How, Yim yimkh@seekasia.com

# Install freetds for pymssql
RUN apt-get -y install freetds-dev freetds-bin
ENV PYMSSQL_BUILD_WITH_BUNDLED_FREETDS=1

# Setup the db-fetch-sgream repository to run
RUN mkdir -p /var/db-fetch-stream/
COPY . /var/db-fetch-stream/
RUN mkdir -p /var/db-fetch-stream/log/
RUN mkdir -p /var/db-fetch-stream/last-state/
RUN pip install -r /var/db-fetch-stream/requirements.txt

# Setup crontab in the docker container
RUN apt-get update && apt-get -y install cron
ENV PYTHONPATH=/var/db-fetch-stream/
COPY ./crontab.txt /etc/cron.d/db-fetch-stream
RUN chmod 0644 /etc/cron.d/db-fetch-stream
RUN touch /var/log/db_fetch_stream.log

# Run the command on container startup
CMD cron && tail -f /var/log/db_fetch_stream.log