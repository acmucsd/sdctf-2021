# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
FROM gcr.io/kctf-docker/challenge@sha256:6dd60da626bc43bf3175d9d7436006db5acc7710d5d1b7006ab53e718fe51e40 as base
RUN apt-get update \
    && apt-get install -yq --no-install-recommends \
       curl ca-certificates socat gnupg lsb-release build-essential python \
    && curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -yq --no-install-recommends nodejs \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY package.json .
COPY package-lock.json .
RUN npm set progress=false && npm config set depth 0
RUN npm install

FROM base
COPY .rename.me.git ./.git
COPY .gitignore .
COPY admin.html .
COPY app.js .
COPY image1.png .
COPY index.html .
COPY robots.txt .
COPY users.db .
COPY secret.flag .

CMD kctf_setup \
    && kctf_drop_privs node /app/app.js
