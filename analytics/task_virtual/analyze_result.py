# Exceptions
from base.constants.test_weighting import TestWeighting
from base.constants.type_visual_test import TypeVisualTest
from base.exceptions import BusinessRuleException

"""
2da Regla
Calcular el porcentaje de aciertos prueba de ishihara
"""
def calculate_porcentaje_hits(total_answers = 1, success_answers = 1  ):
    if total_answers <=  0 or success_answers <= 0:
        raise BusinessRuleException(message_english="Values should be greater than zero.", message_spanish="Los valores deben ser mayores que cero.")

    porcentaje_hits = success_answers * 100 / total_answers

    return porcentaje_hits


def virtual_task_calculate_porcentaje_all_test(virtual_task_list):
    summary = []
    for virtual_task_data in virtual_task_list:
        porcentaje_hits = calculate_porcentaje_hits(total_answers=(virtual_task_data.total_hits+virtual_task_data.total_errors),  success_answers=virtual_task_data.total_hits)

        test_weighting = 0
        if virtual_task_data.code_virtual_task == TypeVisualTest.VISUAL_DEPTH_PERCEPTION.value:
            test_weighting = TestWeighting.VISUAL_DEPTH_PERCEPTION_WEIGHTING.value
        elif virtual_task_data.code_virtual_task == TypeVisualTest.VISUAL_PERCEPTION_OF_COLOR.value:
            test_weighting = TestWeighting.VISUAL_PERCEPTION_OF_COLOR_WEIGHTING.value

        summary.append({
            "code_virtual_task": virtual_task_data.code_virtual_task,
            "total_hits": virtual_task_data.total_hits,
            "total_errors": virtual_task_data.total_errors,
            "porcentaje_hits": porcentaje_hits,
            "test_weighting": test_weighting
        })
    
    return summary