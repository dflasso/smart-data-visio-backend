# Models
from classic_test.models import LangIshiharaResult

# Exceptions
from base.exceptions import NotFoundException, ModelOperationException
from django.core.exceptions import ObjectDoesNotExist

# Contants
from base.constants import TypeAppError

# logger
from base.logger import log_error

# import module sys to get the type of exception
import sys


class LangIshiharaResultsDao():
    """Implements functions custom of lang_ishihara's CRUD"""

    @staticmethod
    def save_or_update_by_id_ticket_patient_tests(**results_model):
        lang_ishihara_result = LangIshiharaResult(**results_model)
        try:
            result_registered = LangIshiharaResultsDao.find_by_id_ticket_patient_tests_and_type_test(
                                                                    id=results_model['ticket_patient_tests'],
                                                                    type_test=results_model['type_test'],
                                                                )
                                                                
            result_registered.results = result_registered.results + lang_ishihara_result.results
            LangIshiharaResultsDao._save(lang_ishihara_results=result_registered)
            return result_registered
        except (NotFoundException, ModelOperationException):
            return LangIshiharaResultsDao.create_results(**results_model)
        except:
            return LangIshiharaResultsDao.create_results(**results_model)

    @staticmethod
    def _save(lang_ishihara_results):
        try:
            return lang_ishihara_results.save()
        except:
            log_error(action="LangIshiharaResultsDao._save",
                      message="Unexpedted Error in save results",
                      details_error={"trace": sys.exc_info()[0]})

            raise ModelOperationException(message_english=f'Data access failed',
                                          message_spanish=f'Fallo al acceder a los datos.')

    @staticmethod
    def find_by_id_ticket_patient_tests_and_type_test(id, type_test):
        try:
            result = LangIshiharaResult.objects.get(
                ticket_patient_tests=id, type_test=type_test)
            if result is None:
                raise NotFoundException(message_english=f'Test not found by id ticket patient tests = {id}',
                                        message_spanish=f'Prueba no encontrada, con el id del ticket de las pruebas del paciente = {id}',
                                        code=TypeAppError.TEST_LANG_ISHIHARA_NOT_FOUND.value)

            return result
        except ObjectDoesNotExist as e:
            log_error(action="LangIshiharaResultsDao.find_by_id_ticket_patient_tests",
                      message=f"ObjectDoesNotExist Error, found results by id ticket patient tests = {id}",
                      details_error={"trace": e})
            raise NotFoundException(message_english=f'Results of test not found by id ticket patient tests  = {id}',
                                    message_spanish=f'Prueba no encontrada, con el id del ticket de las pruebas del paciente = {id}',
                                    code=TypeAppError.TEST_LANG_ISHIHARA_NOT_FOUND.value)
        except:
            details_error = {
                "type": sys.exc_info()[0],
                "value": sys.exc_info()[1],
                "treceback": sys.exc_info()[2]
            }

            log_error(action="LangIshiharaResultsDao.find_by_id_ticket_patient_tests",
                      message=f"Unexpedted Error in find results by id ticket patient tests = {id}",
                      details_error=details_error)
            raise ModelOperationException(message_english=f'Data access failed',
                                          message_spanish=f'Fallo al acceder a los datos.')

    @staticmethod
    def find_by_id_ticket_patient_tests(id):
        try:
            result = LangIshiharaResult.objects.get(ticket_patient_tests=id)
            if result is None:
                raise NotFoundException(message_english=f'Test not found by id ticket patient tests = {id}',
                                        message_spanish=f'Prueba no encontrada, con el id del ticket de las pruebas del paciente = {id}',
                                        code=TypeAppError.TEST_LANG_ISHIHARA_NOT_FOUND.value)

            return result
        except ObjectDoesNotExist as e:
            log_error(action="LangIshiharaResultsDao.find_by_id_ticket_patient_tests",
                      message=f"ObjectDoesNotExist Error, found results by id ticket patient tests = {id}",
                      details_error={"trace": e})
            raise NotFoundException(message_english=f'Results of test not found by id ticket patient tests  = {id}',
                                    message_spanish=f'Prueba no encontrada, con el id del ticket de las pruebas del paciente = {id}',
                                    code=TypeAppError.TEST_LANG_ISHIHARA_NOT_FOUND.value)
        except:
            details_error = {
                "type": sys.exc_info()[0],
                "value": sys.exc_info()[1],
                "treceback": sys.exc_info()[2]
            }

            log_error(action="LangIshiharaResultsDao.find_by_id_ticket_patient_tests",
                      message=f"Unexpedted Error in find results by id ticket patient tests = {id}",
                      details_error=details_error)
            raise ModelOperationException(message_english=f'Data access failed',
                                          message_spanish=f'Fallo al acceder a los datos.')

    @staticmethod
    def create_results(**results_as_dict):
        try:
            return LangIshiharaResult.objects.create(**results_as_dict)
        except:
            details_error = {
                "type": sys.exc_info()[0],
                "value": sys.exc_info()[1],
                "treceback": sys.exc_info()[2]
            }

            log_error(action="LangIshiharaResultsDao.create_results",
                      message="Unexpedted Error in save results",
                      details_error=details_error)

            raise ModelOperationException(message_english=f'Data access failed',
                                          message_spanish=f'Fallo al acceder a los datos.')
