from captura_id_instancias_repository import captura_id_instancias
from captura_status_instancias_repository import status_instancias

STATUS_PROCESSAMENTO = ['pending','running']

'''
    Verifica se o estados das intancias criadas estão em processamento, para 
    isso, primeiro realiza uma consulta para captuarar as identificações das 
    instancias em execução, depois realiza uma consulta para saber o estado 
    atual. Ao fim valida se todos estão em um estado de procesamento. 
'''
def em_processamento():
    id_instancias = captura_id_instancias()
    status_list = status_instancias(id_instancias)

    if len(status_list) == 0:
        return False

    for status in status_list: 
        if status not in STATUS_PROCESSAMENTO:
            return False
    return True