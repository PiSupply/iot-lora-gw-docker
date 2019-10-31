#IoT LoRa Controller Docker File
#(C) Pi Supply 2019
#Licensed under the GNU GPL V3 License.

FROM debian:buster-slim

WORKDIR /opt/iotloragateway/controller

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y sqlite3 nginx php7.3-fpm php7.3-sqlite3 php7.3-json php7.3-curl git && \
    git clone https://github.com/PiSupply/iot-lora-controller.git && \
    rm /etc/nginx/sites-enabled/default && \
    rm /etc/nginx/sites-available/default

COPY files/iotloragateway /etc/nginx/sites-available/

RUN ln -s /etc/nginx/sites-available/iotloragateway /etc/nginx/sites-enabled/

EXPOSE 80 443

STOPSIGNAL SIGTERM

COPY files/run.sh .

RUN chmod +x run.sh

ENTRYPOINT ["sh", "/opt/iotloragateway/controller/run.sh"]
