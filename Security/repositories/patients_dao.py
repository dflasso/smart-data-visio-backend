# Model
from Security.models import User

# Exceptions
from base.exceptions import NotFoundException, ModelOperationException
from django.core.exceptions import ObjectDoesNotExist

# Logger
from base.logger import log_error

# Contants
from base.constants import TypeAppError

# import module sys to get the type of exception
import sys

class PatientsDao():
    """Implements operations CRUD only user with profile=(P01 - Patient) """

    @staticmethod 
    def find_by_id_in_list(list_id_patients = []):
        try:
            return User.objects.filter(id__in=list_id_patients)

        except ObjectDoesNotExist as e:
            log_error(action="PatientsDao.find_by_id_in_list",
                      message=f"Pacientes no encontrada",
                      details_error={"trace": e})
            raise NotFoundException(message_english=f'Patients not found',
                                    message_spanish=f'Pacientes no encontradas',
                                    code=TypeAppError.USERS_NOT_FOUND.value)
        except:
            details_error = {
                "type": sys.exc_info()[0],
                "value": sys.exc_info()[1],
                "treceback": sys.exc_info()[2]
            }

            log_error(action="PatientsDao.find_by_id_in_list",
                      message=f"Unexpedted Error in find Patients'",
                      details_error=details_error)
            raise ModelOperationException(message_english=f'Data access failed',
                                          message_spanish=f'Fallo al acceder a los datos.')
    
    @staticmethod 
    def find_by_num_document(num_document = ""):
        try:
             return User.objects.get(doc_identification=num_document)
        except ObjectDoesNotExist as e:
            log_error(action="PatientsDao.find_by_num_document",
                      message=f"Paciente no encontrado",
                      details_error={"trace": e})
            raise NotFoundException(message_english=f'Patients not found',
                                    message_spanish=f'Paciente no encontrado',
                                    code=TypeAppError.USERS_NOT_FOUND.value)
        except:
            details_error = {
                "type": sys.exc_info()[0],
                "value": sys.exc_info()[1],
                "treceback": sys.exc_info()[2]
            }

            log_error(action="PatientsDao.find_by_num_document",
                      message=f"Unexpedted Error in find Patient'",
                      details_error=details_error)
            raise ModelOperationException(message_english=f'Data access failed',
                                          message_spanish=f'Fallo al acceder a los datos.')
    
    @staticmethod 
    def find_by_id(pk = 0):
        try:
             return User.objects.get(id=pk)
        except ObjectDoesNotExist as e:
            log_error(action="PatientsDao.find_by_id",
                      message=f"Paciente no encontrado",
                      details_error={"trace": e})
            raise NotFoundException(message_english=f'Patients not found',
                                    message_spanish=f'Paciente no encontrado',
                                    code=TypeAppError.USERS_NOT_FOUND.value)
        except:
            details_error = {
                "type": sys.exc_info()[0],
                "value": sys.exc_info()[1],
                "treceback": sys.exc_info()[2]
            }

            log_error(action="PatientsDao.find_by_id",
                      message=f"Unexpedted Error in find Patient'",
                      details_error=details_error)
            raise ModelOperationException(message_english=f'Data access failed',
                                          message_spanish=f'Fallo al acceder a los datos.')

    @staticmethod 
    def update(patient_as_dict):
        try:
            patient_saved = PatientsDao.find_by_id(pk=patient_as_dict['id'])
            patient_saved = patient_saved.__dict__ | patient_as_dict
            del patient_saved['_state']
            patient_model = User(**patient_saved)
            patient_model.save()
            return patient_model
        except:
            details_error = {
                "type": sys.exc_info()[0],
                "value": sys.exc_info()[1],
                "treceback": sys.exc_info()[2]
            }

            log_error(action="PatientsDao.update",
                      message=f"Unexpedted Error in save Patient'",
                      details_error=details_error)
            raise ModelOperationException(message_english=f'Data save failed',
                                          message_spanish=f'Fallo al registrar a los datos.')
        