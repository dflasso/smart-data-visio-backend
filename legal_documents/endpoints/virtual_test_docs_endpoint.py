# Django Rest Framework
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action

# Serializers
from legal_documents.serializers import VirtualTestDocsSerializerCreate, VirtualTestDocsSerializerReadOnly
# DAOs
from legal_documents.repositories import VirtualTestDocsDao

class VirtualTestDocsEndpoints(viewsets.ViewSet):
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request):
        virtual_test_doc_serializer = VirtualTestDocsSerializerCreate(data=request.data)
        virtual_test_doc_serializer.is_valid(raise_exception=True)
        virtual_test_doc_model = virtual_test_doc_serializer.save()
        virtual_test_doc_model_serializer = VirtualTestDocsSerializerReadOnly(virtual_test_doc_model)
        return Response(virtual_test_doc_model_serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        vitual_test_doc = VirtualTestDocsDao.find_by_id(id=pk)
        vitual_test_doc_serializer = VirtualTestDocsSerializerReadOnly(vitual_test_doc)
        return Response(vitual_test_doc_serializer.data)
    
    @action(detail=True, methods=['get'])
    def find_by_num_gropu_test(self, request, pk=None):
        vitual_test_docs = VirtualTestDocsDao.find_by_num_group_test(num_test=pk)
        vitual_test_doc_serializer = VirtualTestDocsSerializerReadOnly(vitual_test_docs, many=True)
        return Response(vitual_test_doc_serializer.data)