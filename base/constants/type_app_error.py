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
    CONVERT_RESULTS_LANG_FROM_SERIALIZER_TO_MODEL_NOT_IS_ISHIHARA = "0003"


    """
    Codigo de errores: Modelo lang_ishihara
    Range de errores: 0026 - 0050
    """
    TEST_LANG_ISHIHARA_NOT_FOUND = "0026"

    """
    Codigo de errores: Modelo titmus
    Range de errores: 0051 - 0075
    """
    TEST_TITMUS_RESULTS_NOT_FOUND = "0051"

    """
    Codigo de errores: Modelo Ophthalmological Test
    Range de errores: 0076 - 0100
    """
    TESTS_OPHTHALMOLOGICAL_NOT_FOUND = "0076"

    """
    Codigo de errores: Modelo User
    Range de errores: 0101 - 0125
    """
    USERS_NOT_FOUND = "0101"