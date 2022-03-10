# Django Rest Framework
from analytics.ophthalmological_test.analyze_group_test import analytic_mixin_test, calculate_total_procentaje_hits, find_range_for_suggestion_global_total
from analytics.task_virtual.analyze_result import virtual_task_calculate_porcentaje_all_test
from base.constants.rules import MixinRules
from base.constants.test_weighting import TestWeighting
from base.constants.type_visual_test import TypeVisualTest
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

# DAO
from classic_test.repositories.lang_ishihara_results_dao import LangIshiharaResultsDao

# Models
from virtual_task.models import VirtualTaskResultsModel

# analytics 
from analytics.test_lang import clasic_test_calculate_porcentaje_all_test

#constabts
from base.constants import rules_ophthalmological_all_test

class SuggestionEndpoints(viewsets.ViewSet):
    
    @action(detail=True, methods=['get'])
    def generate_suggestions_group_test_ophthalmological(self, request, pk=None, *args, **kwargs):
        
        virtual_tasks_of_group = VirtualTaskResultsModel.objects.filter(group_test_ophthalmological=pk)
        lang_results = LangIshiharaResultsDao.find_by_id_ticket_patient_tests_and_type_test(id=pk, type_test=TypeVisualTest.LANG.value)
        ishihara_results =  LangIshiharaResultsDao.find_by_id_ticket_patient_tests_and_type_test(id=pk, type_test=TypeVisualTest.ISHIHARA.value)

        summary_lang = clasic_test_calculate_porcentaje_all_test(clasic_test_data=lang_results, weighting=TestWeighting.lANG_WEIGHTING.value)
        summary_ishihara = clasic_test_calculate_porcentaje_all_test(clasic_test_data=ishihara_results, weighting=TestWeighting.ISHIHARA_WEIGHTING.value)

        summary_virtual_task = virtual_task_calculate_porcentaje_all_test(virtual_task_list=virtual_tasks_of_group)

        total_porcentaje = calculate_total_procentaje_hits(summary_lang=summary_lang, summary_ishihara=summary_ishihara, virtual_task_summaries=summary_virtual_task)

        

        msg_total = find_range_for_suggestion_global_total(total_porcentaje_tests=total_porcentaje, rules_groups_test=rules_ophthalmological_all_test)
        msg_lang_depth_perception = analytic_mixin_test(classic_test_summary=summary_lang,
                                                        visual_task_summaries=summary_virtual_task,
                                                        code_mixin_rule=MixinRules.LANG_AND_DEPTH_PERCEPTION.value)
        
        msg_ishihara_perception_color = analytic_mixin_test(classic_test_summary=summary_ishihara,
                                                        visual_task_summaries=summary_virtual_task,
                                                        code_mixin_rule=MixinRules.ISHIHARA_AND_PERCEPTION_OF_COLOR.value)

        suggestions  = []
        suggestions.append(msg_total)
        suggestions.append(msg_lang_depth_perception)
        suggestions.append(msg_ishihara_perception_color)

        return Response({"summary_lang": summary_lang, 
                         "summary_ishihara": summary_ishihara, 
                         "summary_virtual_task": summary_virtual_task,
                         "total_porcentaje": total_porcentaje,
                         "suggestions" : suggestions })