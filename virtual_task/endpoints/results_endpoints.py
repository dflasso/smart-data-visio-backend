# Django Rest Framework
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

# Serializer
from virtual_task.serializers import FileResultsUploadSerializer, VirtualTaskResultsSerializer

# pandas
import pandas as pd

# constants
from base.constants.type_visual_test import TypeVisualTest

class ResultsVirtualTaskEndpoints(viewsets.ViewSet):

    
    @action(detail=True, methods=['put'])
    def color_perception_find_id_by_num_document(self, request, pk=None, *args, **kwargs):
        serializer = FileResultsUploadSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        
        file = serializer.validated_data['file']
        reader = pd.read_csv(file, sep=";")
        
        
        dfPatient =  reader.loc[ reader['Cedula'] == int(pk)  ] 

        if not dfPatient.empty :
            return Response({"id": dfPatient.iloc[0,0] })    


        return Response({"id": None}, status=status.HTTP_404_NOT_FOUND)
    

    @action(detail=True, methods=['put'])
    def color_perception_find_results_by_id_participant(self, request, pk=None, *args, **kwargs):
        serializer = FileResultsUploadSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        
        file = serializer.validated_data['file']
        reader = pd.read_csv(file, sep=";",  skip_blank_lines=True)
               
        df_results =  reader.loc[ reader['CodigoParticipante'] == int(pk)  ] 

        if not df_results.empty:
            df_results = df_results.iloc[-1]

            query_params = request.query_params.dict()

            name_virtual_task = TypeVisualTest.VISUAL_PERCEPTION_OF_COLOR.name
            code_virtual_task = TypeVisualTest.VISUAL_PERCEPTION_OF_COLOR.value
            
            virtual_task_serializer = VirtualTaskResultsSerializer(data = {
                "name_virtual_task": name_virtual_task,
                "code_virtual_task": code_virtual_task,
                "total_hits": df_results['Aciertos'],
                "total_errors": df_results['Errores'],
                "group_test_ophthalmological": query_params['gr_id']
            })
            
            virtual_task_serializer.is_valid(raise_exception=True)
            virtual_task_serializer.save()

            return Response({"hits": df_results['Aciertos'], "misses": df_results['Errores'] })    

        return Response({"hits": 0, "misses": 0 }, status=status.HTTP_404_NOT_FOUND)

    
    @action(detail=True, methods=['put'])
    def depth_vision_find_results_by_num_doc_participant(self, request, pk=None, *args, **kwargs):
        serializer = FileResultsUploadSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        
        file = serializer.validated_data['file']
        reader = pd.read_csv(file, skip_blank_lines=True)
        
        df_results =  reader.loc[ reader['dni'] == int(pk)  ] 

        if not df_results.empty:
            df_results = df_results.iloc[-1]

            query_params = request.query_params.dict()

            name_virtual_task = TypeVisualTest.VISUAL_DEPTH_PERCEPTION.name
            code_virtual_task = TypeVisualTest.VISUAL_DEPTH_PERCEPTION.value
            
            virtual_task_serializer = VirtualTaskResultsSerializer(data = {
                "name_virtual_task": name_virtual_task,
                "code_virtual_task": code_virtual_task,
                "total_hits": df_results['acierto_pos4'],
                "total_errors": (4-df_results['acierto_pos4']),
                "group_test_ophthalmological": query_params['gr_id']
            })
            
            virtual_task_serializer.is_valid(raise_exception=True)
            virtual_task_serializer.save()

            return Response({"hits": df_results['acierto_pos4'], "misses": 4-df_results['acierto_pos4'] })    

        return Response({"hits": 0, "misses": 0 }, status=status.HTTP_404_NOT_FOUND)