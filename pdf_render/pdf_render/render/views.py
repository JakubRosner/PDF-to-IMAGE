from rest_framework import generics
from .serializer import (
    CreateFileSerializer,
    RetrieveFileSerializer,
    PDFImageSerializer,
)
from .models import File, PDFImages
from .tasks import proces_pdf
from django.db.models import Count


class CreateFile(generics.CreateAPIView):
    serializer_class = CreateFileSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        # delay is set high so we can check if status is changed
        proces_pdf.apply_async((response.data['id'], ), countdown=5)
        return response


class RetrieveFile(generics.RetrieveAPIView):
    serializer_class = RetrieveFileSerializer
    lookup_field = 'id'
    queryset = File.objects.all().annotate(n_pages=Count('pdfimages'))


class RetrieveImage(generics.RetrieveAPIView):
    serializer_class = PDFImageSerializer

    def get_object(self):
        file_id = self.kwargs.get('file_id')
        number = self.kwargs.get('number')
        return PDFImages.objects.get(file_id=file_id, number=number)
