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

# Models
from classic_test.models import TitmusHouseFly

class ConverterTitmusResultsRequest():
    @staticmethod
    def from_req_update_fly_results(**request):
        try: 
            titmus_result_saved =  TitmusResultsDao.find_by_ticket_patient_tests(ticket_patient=request['ticket_patient_tests'])
            titmus_result_saved.house_fly = request['house_fly']
            TitmusResultsDao.save(titmus_result_saved)
            return titmus_result_saved
        except (NotFoundException, ModelOperationException): 
            return TitmusResultsDao.create(**request)
        except: 
            return TitmusResultsDao.create(**request)

    @staticmethod
    def from_req_update_animals_results(**request):
        pass

    @staticmethod
    def from_req_update_circles_results(**request):
        pass