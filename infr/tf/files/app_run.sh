#! /bin/bash
yum install docker -y
service docker start

mkdir /opt/manchetes/baixar_html

aws s3 cp --recursive s3://dados-de-manchetes-code-base/baixar_html /opt/manchetes/baixar_html

cd /opt/manchetes/baixar_html/src

bash /opt/manchetes/baixar_html/docker/install-docker.sh
bash /opt/manchetes/baixar_html/docker/run-docker-local.sh >> /opt/manchetes/baixar_html/saida.txt

shutdown now