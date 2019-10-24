#IoT LoRa Controller Docker File
#(C) Pi Supply 2019
#Licensed under the GNU GPL V3 License.

FROM debian:buster-slim

WORKDIR /opt/iotloragateway/controller

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y sqlite3 nginx php7.3-fpm php7.3-sqlite3 php7.3-json php7.3-curl git

RUN git clone https://github.com/PiSupply/iot-lora-controller.git

RUN ls

WORKDIR /etc/nginx/sites-enabled

RUN rm default

WORKDIR /etc/nginx/sites-available

RUN rm default

COPY files/iotloragateway .

RUN ln -s /etc/nginx/sites-available/iotloragateway /etc/nginx/sites-enabled/

EXPOSE 80 443

RUN nginx
