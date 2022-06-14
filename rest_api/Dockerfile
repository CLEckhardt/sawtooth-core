# Copyright 2018 Cargill Incorporated
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# docker build -f rest_api/Dockerfile -t sawtooth-rest-api-local .

# -------------=== rest_api build ===-------------

FROM ubuntu:bionic

RUN apt-get update \
 && apt-get install gnupg -y

RUN echo "deb http://repo.sawtooth.me/ubuntu/nightly bionic universe" >> /etc/apt/sources.list \
 && (apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 44FC67F19B2466EA \
 || apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 44FC67F19B2466EA) \
 && apt-get update


RUN apt-get install -y -q \
    git \
    python3-pip \
    python3-stdeb \
    pkg-config

RUN apt-get update -qq \
    && apt-get install -y -qq python3.7

RUN rm /usr/bin/python3 \
 && ln -s /usr/bin/python3.7 /usr/bin/python3 \
 && ln -s /usr/bin/python3.7 /usr/local/bin/python3 \
 && apt-get install -y \
    python3-pip \
    python-dev \
    python3.7-dev \
 && python3 -m pip install pip --upgrade

RUN python3 -m pip install \
    grpcio \
    grpcio-tools \
    protobuf \
    pyformance \
    cchardet

RUN python3 -m pip install --upgrade setuptools


RUN apt-get install -y -q \
    python3-aiodns \
    python3-aiohttp \
    python3-colorlog \
    python3-toml \
    python3-yaml \
    python3-zmq

RUN mkdir -p /var/log/sawtooth

ENV PATH=$PATH:/project/sawtooth-core/bin

WORKDIR /project/sawtooth-core

CMD echo "\033[0;32m--- Building rest_api ---\n\033[0m" \
 && bin/protogen \
 && cd rest_api \
 && python3 setup.py clean --all \
 && python3 setup.py build
