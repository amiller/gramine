FROM gramineproject/gramine:v1.5

RUN apt-get update
RUN apt-get install -y make gcc

RUN gramine-sgx-gen-private-key
WORKDIR /root/

ADD scripts/ ./scripts/
ADD python.manifest.template ./
ADD Makefile ./
ADD helper-files/ ./helper-files

RUN SGX=1 make

ENTRYPOINT []
CMD ["gramine-sgx-sigstruct-view", "python.sig"]

