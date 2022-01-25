# Models
from patients.models import MedicalHistory
# Exceptions
from base.exceptions import NotFoundException, ModelOperationException
from django.core.exceptions import ObjectDoesNotExist

# Logger
from base.logger import log_error

# Contants
from base.constants import TypeAppError

# import module sys to get the type of exception
import sys


class MedicalHistoryDao():

    @staticmethod
    def find_by_id_patient(patient_id=None):
        """Return medical history of patient"""
        try:
            return MedicalHistory.objects.get(patient_id=patient_id)
        except ObjectDoesNotExist as e:
            log_error(action="MedicalHistoryDao.find_by_id_patient",
                      message=f"Historial medico del Paciente no encontrado",
                      details_error={"trace": e})
            raise NotFoundException(message_english=f'Medical History not found',
                                    message_spanish=f'Hstorial medico no encontrado',
                                    code=TypeAppError.TESTS_OPHTHALMOLOGICAL_NOT_FOUND.value)
        except:
            details_error = {
                "type": sys.exc_info()[0],
                "value": sys.exc_info()[1],
                "treceback": sys.exc_info()[2]
            }

            log_error(action="MedicalHistoryDao.find_by_id_patient",
                      message=f"Unexpedted Error in find Medical History'",
                      details_error=details_error)
            raise ModelOperationException(message_english=f'Data access failed',
                                          message_spanish=f'Fallo al acceder a los datos.')

    @staticmethod
    def create_after_save_patient(eyeglasses, diseases, id_patient="0"):
        try:
            eyeglasses_as_dict = dict(eyeglasses)
            if type(eyeglasses_as_dict) is dict and type(diseases) is list:
                
                new_medical_history = {
                    "patient_id": id_patient,
                    "eyeglasses": eyeglasses_as_dict,
                    "diseases": diseases
                }
                return MedicalHistoryDao.create_or_update(**new_medical_history)
            else:
                raise ModelOperationException(message_english=f'Data format failed',
                                          message_spanish=f'Formato de los datos incorrectos')
        except:
            details_error = {
                "type": sys.exc_info()[0],
                "value": sys.exc_info()[1],
                "treceback": sys.exc_info()[2]
            }

            log_error(action="MedicalHistoryDao.create_after_save_patient",
                      message=f"Unexpedted Error in find Medical History",
                      details_error=details_error)
            raise ModelOperationException(message_english=f'Data access failed',
                                          message_spanish=f'Fallo al acceder a los datos.')


    @staticmethod
    def create_or_update(**medical_history_as_dict):
        try:
            medical_history_model = MedicalHistoryDao.find_by_id_patient(
                patient_id=medical_history_as_dict['patient_id'])

            new_data_medical_history =  MedicalHistory(**medical_history_as_dict)
            
            if new_data_medical_history.eyeglasses is not None:
                medical_history_model.eyeglasses = new_data_medical_history.eyeglasses
            
            if new_data_medical_history.diseases is not None:
                medical_history_model.diseases = new_data_medical_history.diseases
            
            return MedicalHistoryDao.save(medical_history_model)
        except (NotFoundException, ModelOperationException):
            return MedicalHistoryDao.create(**medical_history_as_dict)
        except:
            details_error = {
                "type": sys.exc_info()[0],
                "value": sys.exc_info()[1],
                "treceback": sys.exc_info()[2]
            }

            log_error(action="MedicalHistoryDao.create_or_update",
                      message=f"Unexpedted Error in find Medical History",
                      details_error=details_error)
            return MedicalHistoryDao.create(**medical_history_as_dict)
    
    @staticmethod 
    def save(medical_history_model):
        try:
            medical_history_model.save()
            return medical_history_model
        except:
            details_error = {
                "type": sys.exc_info()[0],
                "value": sys.exc_info()[1],
                "treceback": sys.exc_info()[2]
            }

            log_error(action="MedicalHistoryDao.save",
                      message="Unexpedted Error in save results",
                      details_error=details_error)

            raise ModelOperationException(message_english=f'Data access failed',
                                          message_spanish=f'Fallo al acceder a los datos.')


    @staticmethod 
    def create(**medical_history_as_dict):
        try:
            return MedicalHistory.objects.create(**medical_history_as_dict)
        except:
            
            details_error = {
                "type": sys.exc_info()[0],
                "value": sys.exc_info()[1],
                "treceback": sys.exc_info()[2]
            }

            log_error(action="MedicalHistoryDao.create",
                      message="Unexpedted Error in save results",
                      details_error=details_error)

            raise ModelOperationException(message_english=f'Data access failed',
                                          message_spanish=f'Fallo al acceder a los datos.')