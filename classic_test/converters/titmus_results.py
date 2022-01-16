"""
Permiter convertir las petiticiones de actualizar 
en los datos de los resultados de titmus 
en el objeto del modelo
"""
# Exceptions
from classic_test.models import titmus_results_model
from base.exceptions import NotFoundException, ModelOperationException

# DAOs
from classic_test.repositories import TitmusResultsDao


class ConverterTitmusResultsRequest():
    @staticmethod
    def from_req_update_fly_results(**request):
        return ConverterTitmusResultsRequest.converte_req_to_model(obj_result_name="house_fly",request=request)

    @staticmethod
    def from_req_update_animals_results(**request):
        return ConverterTitmusResultsRequest.converte_req_to_model(obj_result_name="animals_test",request=request)

    @staticmethod
    def from_req_update_circles_results(**request):
        return ConverterTitmusResultsRequest.converte_req_to_model(obj_result_name="circles_test",request=request)

    @staticmethod
    def converte_req_to_model(request , obj_result_name = ""):
        try: 
            titmus_result_saved =  TitmusResultsDao.find_by_ticket_patient_tests(ticket_patient=request['ticket_patient_tests'])

            if obj_result_name == "house_fly":
                titmus_result_saved.house_fly = request[obj_result_name]
            elif obj_result_name == "animals_test":
                titmus_result_saved.animals_test = request[obj_result_name]
            elif obj_result_name == "circles_test":
                titmus_result_saved.circles_test = request[obj_result_name]
            
            TitmusResultsDao.save(titmus_result_saved)
            return titmus_result_saved
        except (NotFoundException, ModelOperationException): 
            return TitmusResultsDao.create(**request)
        except: 
            return TitmusResultsDao.create(**request)
    