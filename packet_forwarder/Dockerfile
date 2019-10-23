FROM debian:buster-slim AS buildstep

WORKDIR /opt/iotloragateway/packet_forwarder

RUN apt-get update && apt-get upgrade -y

RUN apt-get -y install protobuf-compiler \
  libprotobuf-dev \
  libprotoc-dev \
  automake \
  libtool \
  autoconf \
  git \
  pkg-config \
  protobuf-c-compiler \
  libprotobuf-c-dev \
  build-essential \
  libc6-dev

COPY buildfiles buildfiles

RUN chmod +x ./buildfiles/packetCompile.sh
RUN ./buildfiles/packetCompile.sh

FROM debian:buster-slim

WORKDIR /opt/iotloragateway/packet_forwarder

RUN apt-get update && apt-get upgrade -y

RUN apt-get -y install libprotobuf-dev libprotoc-dev libprotobuf-c1

COPY --from=buildstep /opt/iotloragateway/packetforwarder_hat .
COPY --from=buildstep /opt/iotloragateway/packetforwarder_sg0 .
COPY --from=buildstep /opt/iotloragateway/packetforwarder_sg1 .
COPY --from=buildstep /opt/iotloragateway/dev/iot-lora-gateway/template_configs/EU-global_conf.json ./global_conf.json
COPY --from=buildstep /opt/iotloragateway/dev/iot-lora-gateway/template_configs/local_conf.json.template ./local_conf.json
COPY --from=buildstep /usr/local/lib/libpaho-embed-* /usr/lib/
COPY --from=buildstep /usr/lib/libttn* /usr/lib/



RUN chmod 777 ./local_conf.json
RUN chmod +x ./packetforwarder_hat
RUN chmod +x ./packetforwarder_sg0
RUN chmod +x ./packetforwarder_sg1

RUN ls -a

CMD ./packetforwarder_sg0
