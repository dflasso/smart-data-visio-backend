# Models
from legal_documents.models import VirtualTestDocs
# Exceptions
from base.exceptions import NotFoundException, ModelOperationException
from django.core.exceptions import ObjectDoesNotExist

# Contants
from base.constants import TypeAppError

class VirtualTestDocsDao():

    @staticmethod
    def find_by_num_group_test(num_test = ""):
        try:
            return VirtualTestDocs.objects.all().filter(num_test=num_test)
        except ObjectDoesNotExist:
            raise NotFoundException(message_english=f'Docs of Test not found by num = {num_test} and type doc = {code_type_doc}',
                                    message_spanish=f'Prueba no encontrada, con el numero = {num_test} y el tipo de documento = {code_type_doc}',
                                    code=TypeAppError.TEST_LANG_ISHIHARA_NOT_FOUND.value)
        except Exception:
            raise ModelOperationException(message_english=f'Data access failed',
                                          message_spanish=f'Fallo al acceder a los datos.')


    @staticmethod
    def find_by_id(id = 0):
        try:
            return VirtualTestDocs.objects.get(id=id)
        except ObjectDoesNotExist:
            raise NotFoundException(message_english=f'Docs of Test not found by id = {id}',
                                    message_spanish=f'Prueba no encontrada, con el id = {id}',
                                    code=TypeAppError.TEST_LANG_ISHIHARA_NOT_FOUND.value)
        except Exception:
            raise ModelOperationException(message_english=f'Data access failed',
                                          message_spanish=f'Fallo al acceder a los datos.')