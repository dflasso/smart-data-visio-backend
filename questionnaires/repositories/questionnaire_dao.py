from questionnaires.models import QuestionnaireModel
# Exceptions
from base.exceptions import NotFoundException, ModelOperationException
from django.core.exceptions import ObjectDoesNotExist

# Logger
from base.logger import log_error

# Contants
from base.constants import TypeAppError

# import module sys to get the type of exception
import sys

class QuestionnaireDAO():

    @staticmethod 
    def find_by_num_test_group_and_code_virtual_task(num_test_group = "", code_virtual_task = "", type = "", version =""):
        try:
            return QuestionnaireModel.objects.all().filter(
                    num_test_group=num_test_group, 
                    code_virtual_task=code_virtual_task,
                    type=type,
                    version=version
                    )
        except ObjectDoesNotExist as e:
            log_error(action="QuestionnaireDAO.find_all_by_patient_id_distinct",
                      message=f"Cuestionario y respuestas no encontradas",
                      details_error={"trace": e})
            raise NotFoundException(message_english=f'Questionary not found',
                                    message_spanish=f'Cuestionario y respuestas no encontradas',
                                    code=TypeAppError.TESTS_OPHTHALMOLOGICAL_NOT_FOUND.value)
        except:
            details_error = {
                "type": sys.exc_info()[0],
                "value": sys.exc_info()[1],
                "treceback": sys.exc_info()[2]
            }

            log_error(action="OphthalmologicalTestDao.find_all_by_patient_id_distinct",
                      message=f"Unexpedted Error in find Test Ophthalmological'",
                      details_error=details_error)
            raise ModelOperationException(message_english=f'Data access failed',
                                          message_spanish=f'Fallo al acceder a los datos.')
        
    @staticmethod 
    def create(**data_as_dict):
        try:
            return QuestionnaireModel.objects.create(**data_as_dict)
        except:
            details_error = {
                "type": sys.exc_info()[0],
                "value": sys.exc_info()[1],
                "treceback": sys.exc_info()[2]
            }

            log_error(action="QuestionnaireDAO.create",
                      message=f"Unexpedted Error in create results questionnarie ",
                      details_error=details_error)
            raise ModelOperationException(message_english=f'Data access failed',
                                          message_spanish=f'Fallo al acceder a los datos.')