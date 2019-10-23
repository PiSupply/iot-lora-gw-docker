FROM debian:buster-slim AS buildstep

WORKDIR /opt/iotloragateway/

RUN apt-get update

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
