FROM python:latest

RUN apt-get update -y && \
    apt-get install python3-opencv -y 

WORKDIR /home/src

COPY . ./
RUN pip install --no-cache-dir -r requirements.txt
#pip install -r requirements.txt

#docker pull alvarodorado/uao-neumonia-main:latest