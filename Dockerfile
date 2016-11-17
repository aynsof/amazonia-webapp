#FROM python:3.5-alpine
FROM geoscienceaustralia/autobots-pipeline
ADD . .
RUN yum install -y git
RUN git clone https://github.com/GeoscienceAustralia/amazonia.git
RUN cd amazonia
RUN pip install -e . --user
RUN cd ..
RUN pip install -r ./requirements.txt
ENV PYTHONUNBUFFERED 1
CMD gunicorn -b 0.0.0.0:8080 -w 4 hello:app --log-file - --access-logfile -
