# Django rest framwork
from rest_framework import status

# Base Custom exception
from base.exceptions.business_rule_exception import BusinessRuleException

# Constants
from base.constants import TypeAppError
from classic_test.constants import TypeClassicTest

# Repositories
from classic_test.repositories import LangIshiharaDao

# Analythics
from analytics.test_lang import analyze_many_answers as lang_analyze_answers

def lang_results_from_serializer_to_model(results_as_dict):
    """Try to converter from request to data ready to save"""
    return _from_serializer_to_model(results_as_dict=results_as_dict, 
                                    type_test=TypeClassicTest.LANG, 
                                    code_error=TypeAppError.CONVERT_RESULTS_LANG_FROM_SERIALIZER_TO_MODEL_NOT_IS_LANG.value)

def ishihara_results_from_serializer_to_model(results_as_dict):
    """Try to converter from request to data ready to save"""
    return _from_serializer_to_model(results_as_dict=results_as_dict, 
                                    type_test=TypeClassicTest.ISHIHARA, 
                                    code_error=TypeAppError.CONVERT_RESULTS_LANG_FROM_SERIALIZER_TO_MODEL_NOT_IS_ISHIHARA.value)

def _from_serializer_to_model(results_as_dict, type_test, code_error):
    """Try to converter from request to data ready to save"""

    _check_type_param(results_as_dict)
    
    _check_type_test(type_test=type_test, 
                     results_as_dict=results_as_dict, 
                     code_error=code_error)
    
    results = []
    for card_test in results_as_dict['results']:
        """Find corrects answer of the test applied"""
        card_test_lang = LangIshiharaDao.find_test_by_id_and_type(card_test['id_test'], type_test.value)
        items_card = lang_analyze_answers(card_test_lang.items_card, card_test['items_card'])
        result = _build_dict_results_detail(id_test=card_test['id_test'], 
                                   card_test_name_english=card_test_lang.name_test_english,
                                   card_test_name_spanish=card_test_lang.name_test_spanish,
                                   observations=card_test['observations'],
                                   started_at=card_test['started_at'],
                                   finished_at=card_test['finished_at'],
                                   items_card=items_card)
        results.append(result)
    
    return {
        "ticket_patient_tests": results_as_dict["ticket_patient_tests"],
        "type_test": type_test.value,
        "results" : results
    }


def _check_type_param(results_as_dict):
    if type(results_as_dict) is not dict:
        """Check if param 'results_as_dict' is a dictonary """
        raise BusinessRuleException(message_english="Internal error, when the application wants to serialize data",
                                    message_spanish="Error interno, cuando la aplicaci??n quiere serializar datos",
                                    code= TypeAppError.CONVERT_RESULTS_LANG_FROM_SERIALIZER_TO_MODEL.value,
                                    debug_message=f"Please review param 'results_as_dict' is the type: {type(results_as_dict)}, It must be dictionary.",
                                    status=status.HTTP_400_BAD_REQUEST)

def _check_type_test(type_test, results_as_dict, code_error):
    if results_as_dict['type_test'] != type_test.value:
        """Check if type of the test applied is correct"""
        raise BusinessRuleException(message_english=f"Type of the test will must be {type_test.name}",
                                    message_spanish=f"El tipo de prueba deberia ser {type_test.name}",
                                    code= code_error,
                                    debug_message=f"Please review field of request 'type_test' is {results_as_dict['type_test']}",
                                    status=status.HTTP_400_BAD_REQUEST)

def _build_dict_results_detail(id_test = 0, card_test_name_spanish= "", card_test_name_english="", observations="", started_at=None, finished_at=None, items_card = []):
    return {
        "id_test": str(id_test),
        "card_test_name_spanish": card_test_name_spanish,
        "card_test_name_english":  card_test_name_english,
        "observations": observations,
        "started_at": started_at,
        "finished_at": finished_at,
        "items_card": items_card
    }