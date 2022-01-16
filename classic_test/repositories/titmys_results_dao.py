# Models
from classic_test.models import TitmusResults

# Exceptions
from base.exceptions import NotFoundException, ModelOperationException
from django.core.exceptions import ObjectDoesNotExist

# Contants
from base.constants import TypeAppError

# logger
from base.logger import log_error

# import module sys to get the type of exception
import sys


class TitmusResultsDao():
    """Implements CRUD Operation in Entity Titmus Results"""
    
    @staticmethod 
    def find_by_ticket_patient_tests(ticket_patient = ""):
        try:
            titmus_found = TitmusResults.objects.get(ticket_patient_tests=ticket_patient)
            if titmus_found is None:
                raise NotFoundException(message_english=f'Test not found by id ticket patient tests = {ticket_patient}',
                                        message_spanish=f'Prueba no encontrada, con el id del ticket de las pruebas del paciente = {ticket_patient}',
                                        code=TypeAppError.TEST_TITMUS_RESULTS_NOT_FOUND.value)

            return titmus_found
        except ObjectDoesNotExist as e:
            log_error(action="TitmusResultsDao.find_by_ticket_patient_tests",
                      message=f"ObjectDoesNotExist Error, found results by id ticket patient tests = {ticket_patient}",
                      details_error={"trace": e})
            raise NotFoundException(message_english=f'Results of test not found by id ticket patient tests  = {ticket_patient}',
                                    message_spanish=f'Prueba no encontrada, con el id del ticket de las pruebas del paciente = {ticket_patient}',
                                    code=TypeAppError.TEST_LANG_ISHIHARA_NOT_FOUND.value)
        except:
            details_error = {
                "type": sys.exc_info()[0],
                "value": sys.exc_info()[1],
                "treceback": sys.exc_info()[2]
            }

            log_error(action="TitmusResultsDao.find_by_ticket_patient_tests",
                      message=f"Unexpedted Error in find results by id ticket patient tests = {ticket_patient}",
                      details_error=details_error)
            raise ModelOperationException(message_english=f'Data access failed',
                                          message_spanish=f'Fallo al acceder a los datos.')
        
    @staticmethod 
    def save(titmus_results_model):
        try:
            return titmus_results_model.save()
        except: 
            details_error = {
                "type": sys.exc_info()[0],
                "value": sys.exc_info()[1],
                "treceback": sys.exc_info()[2]
            }

            log_error(action="TitmusResultsDao.save",
                      message=f"Unexpedted Error in save results titmus ",
                      details_error=details_error)
            raise ModelOperationException(message_english=f'Data access failed',
                                          message_spanish=f'Fallo al acceder a los datos.')
    
        
    @staticmethod 
    def create(**results_as_dict):
        try:
            return TitmusResults.objects.create(**results_as_dict)
        except: 
            details_error = {
                "type": sys.exc_info()[0],
                "value": sys.exc_info()[1],
                "treceback": sys.exc_info()[2]
            }

            log_error(action="TitmusResultsDao.create",
                      message=f"Unexpedted Error in create results titmus ",
                      details_error=details_error)
            raise ModelOperationException(message_english=f'Data access failed',
                                          message_spanish=f'Fallo al acceder a los datos.')