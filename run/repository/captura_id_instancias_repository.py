import json
import logging

TF_LOCAL = "../infr/tf/terraform.tfstate.backup"

class cons:
    INSTANCES = "instances"
    TYPE = "type"
    ATTRIBUTES = "attributes"
    ID = "id"

def __carrega_arquivo():
    arq = open(TF_LOCAL, "r")
    return json.load(arq)

def __valida_estrutura(tf_json):
    def valida_estrutura_base(tf_json):    
        if "resources" not in tf_json:
            raise Exception("resources não encontrado")
    
    def valida_estrutura_instancias(tf_json_instancias):
        if "instances" not in tf_json_instancias:
            raise Exception("instances não encontrado")
    
    def valida_estrutura_atributos(tf_json_atributos):
        if "attributes" not in tf_json_atributos:
            raise Exception("attributes não encontrado")
        if "id" not in tf_json_atributos["attributes"]:
            raise Exception("id não encontrado")

    valida_estrutura_base(tf_json)    
    for tf_json_instancias in tf_json["resources"]:
        valida_estrutura_instancias(tf_json_instancias)
        if tf_json_instancias[cons.TYPE] == "aws_instance":
            for tf_json_atributos in tf_json_instancias["instances"]:
                valida_estrutura_atributos(tf_json_atributos)
            

'''
    Captura as identificações das instancia em execução aparti do arquivo de 
    saida da execução do terraform
'''
def captura_id_instancias():
    tf_json = __carrega_arquivo()
    try:
        __valida_estrutura(tf_json)
    except Exception as e:
        logging.error("O arquivo da estrutura apresenta um erro de formatação ")
        logging.exception(e)
        raise e
    
    list_id_instancias = list()

    for tf_json_instancias in tf_json["resources"]:
        if tf_json_instancias[cons.TYPE] == "aws_instance":
            for tf_json_atributos in tf_json_instancias["instances"]:
                id_instancia = tf_json_atributos["attributes"]["id"]
                list_id_instancias.append(id_instancia)    


    return list_id_instancias








