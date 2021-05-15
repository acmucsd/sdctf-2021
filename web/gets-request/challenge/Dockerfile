FROM node:lts-alpine AS base
WORKDIR /app
COPY package.json .
COPY package-lock.json .

FROM base AS dependencies
RUN npm set progress=false && npm config set depth 0
RUN npm install

FROM gcc AS build
COPY primegen.c .
COPY Makefile .
RUN make

FROM ubuntu:20.04 as chroot
RUN /usr/sbin/useradd -u 1000 user

RUN apt-get update \
    && apt-get install -yq --no-install-recommends \
       curl ca-certificates socat gnupg lsb-release \
    && curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -yq --no-install-recommends nodejs \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY --from=dependencies /app/node_modules ./node_modules
COPY --from=build /primegen .
COPY index.js .
COPY index.html .
COPY run.sh .

FROM gcr.io/kctf-docker/challenge@sha256:6dd60da626bc43bf3175d9d7436006db5acc7710d5d1b7006ab53e718fe51e40 as prod_env
RUN apt-get update \
    && apt-get install -yq --no-install-recommends \
       curl ca-certificates socat gnupg lsb-release \
    && curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -yq --no-install-recommends nodejs \
    && rm -rf /var/lib/apt/lists/*

FROM prod_env
COPY --from=chroot / /chroot
COPY web-servers.nsjail.cfg /home/user/web-servers.nsjail.cfg

CMD kctf_setup \
    && kctf_drop_privs nsjail --config /home/user/web-servers.nsjail.cfg --port 1337 -- /app/run.sh