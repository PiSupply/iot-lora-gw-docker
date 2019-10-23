# iot-lora-gw-docker
Docker Files for IoT LoRa Gateway

#packet_forwarder
This container contains the packet forwarder, the same software is compiled 3 times to provide a command to run it on all 3 different SPI busses.

#database_server
This is pretty much just a MySQL Server

#Web Controller
This is the Web based UI we've created, it doesn't require NGINX & PHP to be in their own containers so is all in this single container.
