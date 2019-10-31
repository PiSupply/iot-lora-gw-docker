#IoT LoRa Controller Docker File
#(C) Pi Supply 2019
#Licensed under the GNU GPL V3 License.

FROM debian:buster-slim

WORKDIR /opt/iotloragateway/controller

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y nginx php7.3-fpm  php7.3-json php7.3-curl git curl php7.3-zip

RUN git clone https://github.com/PiSupply/iot-lora-controller.git

RUN rm /etc/nginx/sites-enabled/default & rm /etc/nginx/sites-available/default

WORKDIR /etc/nginx/sites-available

COPY files/iotloragateway .

RUN ln -s /etc/nginx/sites-available/iotloragateway /etc/nginx/sites-enabled/

#Install composer
WORKDIR /opt/iotloragateway/controller
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php -r "if (hash_file('sha384', 'composer-setup.php') === 'a5c698ffe4b8e849a443b120cd5ba38043260d5c4023dbf93e1558871f1f07f58274fc6f4c93bcfd858c6bd0775cd8d1') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
RUN php composer-setup.php
RUN php -r "unlink('composer-setup.php');"
RUN mv composer.phar /usr/local/bin/composer

WORKDIR /opt/iotloragateway/controller/iot-lora-Controller
RUN composer require symfony/yaml


EXPOSE 80 443

STOPSIGNAL SIGTERM

WORKDIR /opt/iotloragateway/controller

COPY files/run.sh .

RUN chmod +x run.sh

ENTRYPOINT ["sh", "/opt/iotloragateway/controller/run.sh"]
