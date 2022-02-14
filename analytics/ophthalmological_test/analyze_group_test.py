# Exceptions
from base.exceptions import BusinessRuleException

"""

Parametros: 

La funcion recive un arreglo de objetos
{
    "test_name": "", /// Nombre de la prueba
    "test_code": "", /// Código de la prueba
    "test_type": "", /// Tipo de prueba (Virtual o Tradicional)
    "test_weighting": 0.0 /// peso a nivel grupal de la prueba (del 0 al  100)
    "porcentaje_success_answers": 0.0 ///Porcentaje del número de respuestas correctas en relación al total de items  (del 0 al  100)
}

Validaciones:
- La función valida que la sumatoria de los pesos de las pruebas sean igual a 100%

"""
def calculate_total_procentaje_hits(test_results=[]):
    total_test_weighting = 0
    total_porcentaje_tests = 0

    for one_test_result in test_results:
        total_test_weighting += one_test_result['test_weighting']

        # Validación que los pesos no pasen de 100
        if total_test_weighting > 100:
            raise BusinessRuleException(message_english="weightings don't should be greater than one hundred.",
                                        message_spanish="Los pesos no deben ser mayores que cien.")

        porcentaje_global_test = one_test_result['porcentaje_success_answers'] * 100 / one_test_result['test_weighting']
        total_porcentaje_tests += porcentaje_global_test

    # Validación que los pesos sumen  100
    if total_test_weighting != 100:
        raise BusinessRuleException(message_english="weightings don't should be less than one hundred.",
                                    message_spanish="Los pesos no deben ser mayores que cien.")
    
    return total_porcentaje_tests


"""
Parametros
- 'total_porcentaje_tests' :  porcentaje total aciertos del grupo de pruebas visuales (del 0 al 100)
- 'total_porcentaje_tests' : listado de diccionarios con los siguientes atributos
{
    "suggestion": "", # Mensaje de la sugerencia o recomendación
    "min_porcentaje": 0.0, # Valor mínimo del porcentaje para dar recomendación o sugerencia
    "max_porcentaje": 0.0 # Valor máximo del porcentaje para dar recomendación o sugerencia
}

"""
def find_range_for_suggestion(total_porcentaje_tests = 0, rules_groups_test = []):
    msg_suggestion = ""
    for rule in rules_groups_test:
        if total_porcentaje_tests >= rule['min_porcentaje'] and total_porcentaje_tests <= rule['max_porcentaje']:
            msg_suggestion = rule['msg_suggestion']
    
    return msg_suggestion