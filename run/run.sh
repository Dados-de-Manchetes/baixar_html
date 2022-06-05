#!/bin/bash

# cria os recursos
cd ../infr/tf
terraform init
terraform apply -var-file="./tfvars/terraform.tfvars" -auto-approve

# espera a execução finalizar
cd ../../run
python3 main.py 

# destroy tudo que contruiu
cd ../infr/tf
terraform destroy -var-file="./tfvars/terraform.tfvars" -auto-approve
