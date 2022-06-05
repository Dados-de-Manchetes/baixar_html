import boto3

class cons:
    INSTANCE_STATUSES = "InstanceStatuses"
    INSTANCE_STATE = "InstanceState"
    NAME = "Name"

def __ec2_client():
    return boto3.client('ec2')

'''
    Com uma sequencia de ids de instancias realiza uma consulta na aws para 
    capturar qual o estado atual das instancias
'''
def status_instancias(instance_ids:list)->list:
    ec2_client = __ec2_client()

    result_dict = ec2_client.describe_instance_status(
        InstanceIds=instance_ids
    )

    status_list = list()

    for result_dict_instancias in result_dict[cons.INSTANCE_STATUSES]:
        status = result_dict_instancias[cons.INSTANCE_STATE][cons.NAME]
        status_list.append(status)
    
    return status_list