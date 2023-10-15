FROM hackinglab/alpine-base-hl:latest

LABEL maintainer=<ivan.buetler@hacking-lab.com>

COPY root /
RUN apk update && apk add --no-cache socat unit sudo curl python3 py3-pip

EXPOSE 80 1345
