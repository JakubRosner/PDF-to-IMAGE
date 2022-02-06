from rest_framework import serializers
from .models import File, PDFImages


class CreateFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = (
            "file",
            "id",
        )


class RetrieveFileSerializer(serializers.ModelSerializer):
    n_pages = serializers.IntegerField(read_only=True)

    class Meta:
        model = File
        fields = (
            'n_pages',
            'status',
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['n_pages'] = instance.pdfimages_set.count()
        return data


class PDFImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFImages
        fields = (
            'image',
        )
