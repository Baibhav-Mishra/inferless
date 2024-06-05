FROM mysql:latest
ENV MYSQL_ROOT_PASSWORD pass
ADD data.sql /docker-entrypoint-initdb.d
