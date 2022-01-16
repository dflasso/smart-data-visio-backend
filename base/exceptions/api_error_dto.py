"""Estandarizar el objeto de respuesta de las API"""
# Django rest framwork
from rest_framework import status

class SubError():
    def __init__(self, 
                 message_spanish,
                 message_english,
                 code = "0000",
                 field_name_error = ""
                 ):
        self._message_spanish = message_spanish 
        self._message_english = message_english 
        self._code = code
        self._field_name_error = field_name_error
    
    """Getters"""

    @property
    def message_spanish(self):
        return self._message_spanish
    
    @property
    def message_english(self):
        return self._message_english

    @property
    def code(self):
        return self._code
        
    @property
    def field_name_error(self):
        return self._field_name_error
    
    """Setters"""

    @message_spanish.setter
    def set_message_spanish(self, message_spanish):
        self._message_spanish = message_spanish
    
    @message_english.setter
    def set_message_english(self, message_english):
        self._message_english = message_english
    
    @code.setter
    def set_code(self, code):
        self._code = code
    
    @field_name_error.setter
    def set_field_name_error(self, field_name_error):
        self._field_name_error = field_name_error


class ApiError():
    """
    Object standard of response in errors. 
    Obligatories fields: message_spanish, message_english and code
    """

    def __init__(self,
                 message_spanish,
                 message_english,
                 code,
                 status=status.HTTP_400_BAD_REQUEST,
                 debug_message="Internal Error, please look logs.",
                 sub_errors=[]):

        self._message_spanish = message_spanish
        self._message_english = message_english
        self._code = code
        self._http_status = status
        self._debug_message = debug_message
        self._sub_errors = sub_errors

    """Getters"""

    @property
    def message_spanish(self):
        return self._message_spanish
    
    @property
    def message_english(self):
        return self._message_english

    @property
    def code(self):
        return self._code
        
    @property
    def http_status(self):
        return self._http_status
    
    @property
    def debug_message(self):
        return self._debug_message

    @property
    def sub_errors(self):
        return self._sub_errors
    
    """Setters"""

    @message_spanish.setter
    def message_spanish(self, message_spanish):
        self._message_spanish = message_spanish
    
    @message_english.setter
    def message_english(self, message_english):
        self._message_english = message_english
    
    @code.setter
    def code(self, code):
        self._code = code
    
    @http_status.setter
    def http_status(self, http_status):
        self._status = http_status
    
    @debug_message.setter
    def debug_message(self, debug_message):
        self._debug_message = debug_message
    
    
    def add_sub_error(self, sub_error):
        if self._sub_errors is None:
            self._sub_errors = []

        self._sub_errors.append(sub_error)

    @staticmethod
    def build_from_dict(**api_error_dict):
        api_error = ApiError(message_english="", message_spanish="", code="")
        if type(api_error_dict) is dict:
            for key, value in api_error_dict.items():
                if key == "message_spanish":
                    api_error.message_spanish = value
                elif key == "message_english":
                    api_error.message_english = value
                elif key == "code":
                    api_error.code = value
                elif key == "status":
                    api_error.http_status = value
                elif key == "_debug_message":
                    api_error.debug_message = value
        return api_error
        