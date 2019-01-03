FROM {{DOCKERFILE_BASE_IMAGE}}

ENV SINGNET_REPOS=/opt/singnet
ENV GH_REPO_NAME={{GITHUB_REPOSITORY}}
ENV SERVICES_FOLDER=${SINGNET_REPOS}/${GH_REPO_NAME}/{{SERVICES_FOLDER}}
ENV SERVICE_NAME={{SERVICE_NAME}}
ENV SNETD_HOST={{SERVICE_DAEMON_HOST}}
ENV SNETD_PORT={{SERVICE_DAEMON_PORT}}
ENV SNETD_CONFIG=snetd.config.json

RUN mkdir -p ${SINGNET_REPOS}

RUN apt-get update && \
    apt-get install -y \
    git \
    wget \
    nano \
    libudev-dev \
    libusb-1.0-0-dev

RUN apt-get install -y python3 python3-pip
RUN apt-get install -y nodejs npm

RUN cd ${SINGNET_REPOS} && \
    git clone https://github.com/singnet/snet-cli && \
    cd snet-cli && \
    ./scripts/blockchain install && \
    pip3.6 install -e .

RUN cd ${SINGNET_REPOS} && \
    mkdir snet-daemon && \
    cd snet-daemon && \
    wget https://github.com/singnet/snet-daemon/releases/download/v{{SNETD_VERSION}}/snetd-{{SNETD_VERSION}}.tar.gz && \
    tar -xvf snetd-{{SNETD_VERSION}}.tar.gz && \
    mv linux-amd64/snetd /usr/bin/snetd

RUN cd ${SINGNET_REPOS} && \
    git clone https://github.com/{{GITHUB_ACCOUNT}}/{{GITHUB_REPOSITORY}}.git

RUN cd ${SERVICES_FOLDER}/${SERVICE_NAME} && \
    sh -c "echo '{ \"DAEMON_END_POINT\": \"http://${SNETD_HOST}:${SNETD_PORT}\", \
                   \"ETHEREUM_JSON_RPC_ENDPOINT\": \"https://kovan.infura.io\", \
                   \"IPFS_END_POINT\": \"http://ipfs.singularitynet.io:80\", \
                   \"REGISTRY_ADDRESS_KEY\": \"{{REGISTRY_ADDRESS}}\", \
                   \"PASSTHROUGH_ENABLED\": true, \
                   \"PASSTHROUGH_ENDPOINT\": \"http://localhost:7003\", \
                   \"ORGANIZATION_ID\": \"snet\", \
                   \"SERVICE_ID\": \"${SERVICE_NAME}\", \
                   \"LOG\": { \
                   \"LEVEL\": \"debug\", \
                   \"OUTPUT\": { \
                       \"TYPE\": \"stdout\" \
                       } \
                   } \
                }'" > ${SNETD_CONFIG}

RUN cd ${SERVICES_FOLDER}/${SERVICE_NAME} && \
    pip3 install -r requirements.txt && \
    sh buildproto.sh

WORKDIR ${SERVICES_FOLDER}/${SERVICE_NAME}