# Models
from ophthalmological_test.models import OphthalmologicalTest

# Exceptions
from base.exceptions import NotFoundException, ModelOperationException
from django.core.exceptions import ObjectDoesNotExist

# Logger
from base.logger import log_error

# Contants
from base.constants import TypeAppError

# import module sys to get the type of exception
import sys

class OphthalmologicalTestDao():

    @staticmethod 
    def find_all_by_patient_id_distinct():
        """Return a List with id of patients, who has a test ophthalmological """
        try:
            distinc = OphthalmologicalTest.objects.all().values('patient_id').distinct()
            items_distin  = [item['patient_id'] for  item in  distinc ]
            return items_distin

        except ObjectDoesNotExist as e:
            log_error(action="OphthalmologicalTestDao.find_all_by_patient_id_distinct",
                      message=f"Pruebas oftalmologicas no encontrada",
                      details_error={"trace": e})
            raise NotFoundException(message_english=f'Test Ophthalmological not found',
                                    message_spanish=f'Pruebas oftalmologicas no encontradas',
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
    def save(ophthalmological_model):
        try:
            return ophthalmological_model.save()
        except: 
            details_error = {
                "type": sys.exc_info()[0],
                "value": sys.exc_info()[1],
                "treceback": sys.exc_info()[2]
            }

            log_error(action="OphthalmologicalTestDao.save",
                      message=f"Unexpedted Error in save results titmus ",
                      details_error=details_error)
            raise ModelOperationException(message_english=f'Data access failed',
                                          message_spanish=f'Fallo al acceder a los datos.')
    
    
    @staticmethod 
    def create(**data_as_dict):
        try:
            return OphthalmologicalTest.objects.create(**data_as_dict)
        except:
            details_error = {
                "type": sys.exc_info()[0],
                "value": sys.exc_info()[1],
                "treceback": sys.exc_info()[2]
            }

            log_error(action="OphthalmologicalTestDao.create",
                      message=f"Unexpedted Error in create results titmus ",
                      details_error=details_error)
            raise ModelOperationException(message_english=f'Data access failed',
                                          message_spanish=f'Fallo al acceder a los datos.')

    @staticmethod 
    def find_groups_test_by_patient_id(patient_id= ""):
        try:
            return OphthalmologicalTest.objects.filter(patient_id=patient_id)
        except:
            details_error = {
                "type": sys.exc_info()[0],
                "value": sys.exc_info()[1],
                "treceback": sys.exc_info()[2]
            }

            log_error(action="OphthalmologicalTestDao.create",
                      message=f"Unexpedted Error in create results titmus ",
                      details_error=details_error)
            raise ModelOperationException(message_english=f'Data access failed',
                                          message_spanish=f'Fallo al acceder a los datos.')