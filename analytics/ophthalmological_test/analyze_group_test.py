# Exceptions
from base.constants.rules import MixinRules
from base.constants.type_visual_test import TypeVisualTest
from base.exceptions import BusinessRuleException

# Constants
from base.constants import rules_ophthalmological_mixin_test


def calculate_total_procentaje_hits(summary_lang, summary_ishihara, virtual_task_summaries = []):
    total_test_weighting = 0

    total_porcentaje_test = 0
    for one_virtual_test_result in virtual_task_summaries:
        total_test_weighting += one_virtual_test_result['test_weighting']
        total_porcentaje_test += one_virtual_test_result['porcentaje_hits'] * one_virtual_test_result['test_weighting'] / 100

    total_test_weighting = total_test_weighting + summary_lang['test_weighting'] +summary_ishihara['test_weighting']
    
    # Validación que los pesos no pasen de 100
    if total_test_weighting > 100:
        raise BusinessRuleException(message_english="weightings don't should be greater than one hundred.",
                                    message_spanish="Los pesos no deben ser mayores que cien.")

    # Validación que los pesos sumen  100
    if total_test_weighting != 100:
        raise BusinessRuleException(message_english="weightings don't should be less than one hundred.",
                                    message_spanish="Los pesos no deben ser mayores que cien.")

    total_porcentaje_test += summary_lang['porcentaje_hits'] * summary_lang['test_weighting'] / 100
    total_porcentaje_test += summary_ishihara['porcentaje_hits'] * summary_ishihara['test_weighting'] / 100

    return total_porcentaje_test



def find_range_for_suggestion_global_total(total_porcentaje_tests=0, rules_groups_test=[]):
    msg_suggestion = ""
    for rule in rules_groups_test:
        if total_porcentaje_tests >=rule['total_min_value'] and total_porcentaje_tests <= rule['total_max_value']:
            msg_suggestion = rule['msg']

    return msg_suggestion



def analytic_mixin_test(classic_test_summary , visual_task_summaries, code_mixin_rule):
    rule_selected = None
    for rule in rules_ophthalmological_mixin_test:
        if code_mixin_rule == rule['code_rule']:
            rule_selected = rule
    
    code_virtual_task_target = ""
    if code_mixin_rule == MixinRules.LANG_AND_DEPTH_PERCEPTION.value:
        code_virtual_task_target = TypeVisualTest.VISUAL_DEPTH_PERCEPTION.value
    elif code_mixin_rule == MixinRules.ISHIHARA_AND_PERCEPTION_OF_COLOR.value:
        code_virtual_task_target = TypeVisualTest.VISUAL_PERCEPTION_OF_COLOR.value
    
    porcentaje_test_virtual = 0
    for visual_task in visual_task_summaries:
        if code_virtual_task_target == visual_task['code_virtual_task']:
            porcentaje_test_virtual = visual_task['porcentaje_hits']
    
    return check_specific_visual_deficiency(porcentaje_test_tradicional=classic_test_summary['porcentaje_hits'],
    porcentaje_test_virtual=porcentaje_test_virtual, rules_groups_test=rule_selected)


def check_specific_visual_deficiency(porcentaje_test_tradicional=0, porcentaje_test_virtual=0, rules_groups_test = {}):
    msg_suggestion = ""
    
    if porcentaje_test_tradicional < rules_groups_test['clasic_test_min_porcentaje'] and porcentaje_test_virtual <= rules_groups_test['virtual_task_min_porcentaje']:
        msg_suggestion = rules_groups_test['msg_in_range']
    else:
        msg_suggestion = rules_groups_test['msg_out_range']

    return msg_suggestion


