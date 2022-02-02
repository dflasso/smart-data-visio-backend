# Django Rest Framework
from rest_framework import viewsets
# Django
from django.http import FileResponse

# Makers
from reports.makers_reports import SuggestionReportMaker

class ReportSugestionEndpoints(viewsets.ViewSet):
    
    def retrieve(self, request, pk=None):
        # Create a file-like buffer to receive PDF data.
        buffer  = SuggestionReportMaker.create()
        return FileResponse(buffer, as_attachment=True, filename='resultados.pdf')