#!/bin/bash
UUID=0714cfb1-7884-4b9f-9cdf-0f594ba728eb
if [ -z "$UUID" ]; then
    echo -n "Enter UUID: "
    read UUID
fi

[ -e dockerfiles.tar.gz ] && rm dockerfiles.tar.gz

if [ -e "$UUID".* ]; then
    tar cvzf dockerfiles.tar.gz Dockerfile $UUID.* root/ challenge-description/ configs/
else
    tar cvzf dockerfiles.tar.gz Dockerfile root/ challenge-description/ configs/
fi

md5sum dockerfiles.tar.gz