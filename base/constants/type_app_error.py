from enum import Enum


class TypeAppError(Enum):
    """
    Codigo de errores en la api: Registro de resultados en LANG
    Range de errores: 0001 - 0025
    """

    """
    Codigo de error que es lanzando cuando a la 
    función de conversión le llegantos datos errones
    """
    CONVERT_RESULTS_LANG_FROM_SERIALIZER_TO_MODEL = "0001"
    CONVERT_RESULTS_LANG_FROM_SERIALIZER_TO_MODEL_NOT_IS_LANG = "0002"


    """
    Codigo de errores: Modelo lang_ishihara
    Range de errores: 0026 - 0027
    """
    TEST_LANG_ISHIHARA_NOT_FOUND = "0026"