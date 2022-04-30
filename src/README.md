# Rodar a aplicação

Pode ser rodada a aplicação no ambiente local utilizando o comando abaixo, porém
será necessário instalar diversos pacotes. Recomendo utilizar o docker.
> python3 main.py

# Rodar a aplicação via docker

Para utilizar no ambiente docker é necessário ter o docker intalado e rodar o 
comando de instalação atravez do comando abaixo.

> ../docker/install-docker.sh 

Já para executar de fato é necessário rodar um dos dois comandos abaixo:

> ../docker/run-docker-local.sh 
> ../docker/run-docker.sh 

A diferença entre eles é que o local, durante a execução, não desanexa do 
terminal.