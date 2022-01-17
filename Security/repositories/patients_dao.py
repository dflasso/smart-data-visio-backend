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
        