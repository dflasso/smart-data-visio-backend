# Models
from classic_test.models.lang_ishihara_model import LangIshiharaTest

# Exceptions
from base.exceptions import NotFoundException, ModelOperationException
from django.core.exceptions import ObjectDoesNotExist

# Contants
from base.constants import TypeAppError

class LangIshiharaDao():
    """Implements functions custom of lang_ishihara's CRUD"""
    
    @staticmethod
    def find_test_by_id(id):
        try:
            test = LangIshiharaTest.objects.all().get(id=id)
            if test is None:
                raise NotFoundException(message_english=f'Test not found by id = {id}',
                                        message_spanish=f'Prueba no encontrada, con el id = {id}',
                                        code=TypeAppError.TEST_LANG_ISHIHARA_NOT_FOUND.value)
            return test
        except ObjectDoesNotExist:
            raise NotFoundException(message_english=f'Test not found by id = {id}',
                                    message_spanish=f'Prueba no encontrada, con el id = {id}',
                                    code=TypeAppError.TEST_LANG_ISHIHARA_NOT_FOUND.value)
        except Exception:
            raise ModelOperationException(message_english=f'Data access failed',
                                          message_spanish=f'Fallo al acceder a los datos.')