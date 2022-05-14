#! /bin/bash
yum install docker -y
service docker start

mkdir /opt/manchetes

aws s3 cp --recursive s3://dados-de-manchetes-code-base/baixar_html /opt/manchetes

cd /opt/manchetes/src

bash /opt/manchetes/docker/install-docker.sh
bash /opt/manchetes/docker/run-docker-local.sh >> /opt/manchetes/saida.txt

shutdown now