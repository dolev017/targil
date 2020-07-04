FROM ubuntu:latest
WORKDIR /tmp
ENV VERSION 1.2.0
RUN apt update -y
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update -y
RUN apt install software-properties-common vim python3.8 zip unzip -y
COPY ./zip_job.py .
CMD ["dpkg","--print-architecture","echo","$OSTYPE"]