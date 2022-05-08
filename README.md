# Baixar html

## Ideia

A ideia desse repositório é conter os códigos para efetuar o download das páginas. A forma que foi escolhido para solucionar o problema é primeiramente criar toda a arquitetura, depois realizar o download das páginas com uma instância, para ao fim destruir tudo que foi criado. O processo de criação e destruição é dado para reduzir os custos. 

Toda a aplicação roda em um container docker. Já o download das páginas é feito por um firefox controlado pelo selenium o qual é ordenado via python. Durante o processo, os códigos das páginas são enviados para um bucket. Dentro do bucket os dados são armazenados como um uuid aleatório, não sendo possível realizar uma busca.


## Organização

### /docker
Pasta com a responsabilidade de organizar os scripts do ciclo de vida do container

### /exec
Conjunto de arquivos que controla o ciclo de vida da aplicação

### /infr
Arquivo referentes a infraestrutura para rodar o projeto

### /src
Local onde apresenta todos os arquivos para a execução da aplicação
