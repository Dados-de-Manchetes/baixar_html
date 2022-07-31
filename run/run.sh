#!/bin/bash

# cria os recursos
cd ../infr/tf
if ! terraform init; then
    echo "Erro ao executar terraform init"
    exit -1
fi

if terraform apply -var-file="./tfvars/terraform.tfvars" -auto-approve; then
    # espera a execução finalizar
    cd ../../run
    if ! python3 main.py; then 
        echo "Erro ao executar o comando"
    fi
    

    # destroy tudo que contruiu
    cd ../infr/tf
else
    echo "Erro ao executar terraform apply"
fi

if ! terraform destroy -var-file="./tfvars/terraform.tfvars" -auto-approve; then
    echo "Erro ao executar terraform destroy"
fi
