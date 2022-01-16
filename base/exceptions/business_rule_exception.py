"""Custom Exception Business Rules"""
# Django rest framwork
from rest_framework import status
from rest_framework.exceptions import APIException

# DTO base of standart exception
from base.exceptions.api_error_dto import ApiError

# Serializer
from base.exceptions.api_error_serializer import ApiErrorSerializer

class BusinessRuleException(APIException):
    """
    BusinessRuleException
    Exception throwable when some business rule or logic validation fail  
    """
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Logic validation failed'
    default_code = 'bad_request'

    def __init__(self,
                 message_spanish=None,
                 message_english=None,
                 code=None,
                 status=status.HTTP_400_BAD_REQUEST,
                 debug_message="Validations errors.",
                 sub_errors=[]):

        self._api_error = ApiError(message_spanish=message_spanish,
                             message_english=message_english,
                             code=code,
                             status = status,
                             debug_message=debug_message,
                             sub_errors=sub_errors
                             )
        self.status_code = status
        api_error_serializer = ApiErrorSerializer(self._api_error)
        self.detail = api_error_serializer.data
        
        
    def __str__(self):
        return str(self._api_error)
    
    def get_full_details(self):
        api_error_serializer = ApiErrorSerializer(self._api_error)
        return api_error_serializer.data