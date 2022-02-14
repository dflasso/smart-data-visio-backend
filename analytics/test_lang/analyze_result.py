# Exceptions
from base.exceptions import BusinessRuleException

def analyze_many_answers(corrects_answers, patient_answers ):
    items_card_results = []
    for correct_answer in corrects_answers:
        for patient_answer in patient_answers:
            if correct_answer['item_id'] == patient_answer['item_id']:
                items_card_results.append( analyze_answer(correct_answer, patient_answer) )
    return items_card_results


def analyze_answer(correct_answer, patient_answer ):
    is_answer_correct = False
    incorrect_answers = []
    for patient_answer_value in patient_answer['answers']:
        """Delete blank space and convert strings into lower case"""
        patient_answer_debugged = _debugged_answer(patient_answer_value)
        correct_answer_spanish = _debugged_answer(correct_answer['description_spanish'])
        correct_answer_english = _debugged_answer(correct_answer['description_english'])

        if patient_answer_debugged == correct_answer_spanish or patient_answer_debugged == correct_answer_english:
            """Check if answer is correct"""
            is_answer_correct = True
        else:
            incorrect_answers.append(patient_answer_value)

    return _build_dict_card_result(corrects_answers=correct_answer, 
                                   is_answer_correct=is_answer_correct, 
                                   incorrect_answers=incorrect_answers)

"""
1era Regla
Calcular el porcentaje de aciertos prueba de lang
"""
def calculate_porcentaje_hits(total_answers = 1, success_answers = 1  ):
    if total_answers <=  0 or success_answers <= 0:
        raise BusinessRuleException(message_english="Values should be greater than zero.", message_spanish="Los valores deben ser mayores que cero.")

    porcentaje_hits = success_answers * 100 / total_answers

    return porcentaje_hits

def _debugged_answer(str_answer):
    answer_debugged = str(str_answer)
    answer_debugged = answer_debugged.replace(" ", "")
    answer_debugged = answer_debugged.casefold()
    return answer_debugged


def _build_dict_card_result(corrects_answers, is_answer_correct, incorrect_answers):
    value_result_answer = 0.0
    if is_answer_correct: 
        value_result_answer = corrects_answers['weighing']
        
    return {
        "item_id": corrects_answers['item_id'],
        "correct_answer_spanish": corrects_answers['description_spanish'],
        "correct_answer_english": corrects_answers['description_english'],
        "value_correct_answer": corrects_answers['weighing'],
        "answer_correct": is_answer_correct,
        "incorrect_answers": incorrect_answers,
        "value_result_answer": value_result_answer
    }