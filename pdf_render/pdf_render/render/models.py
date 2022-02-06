from http.client import PROCESSING
from django.db import models
import uuid


class File(models.Model):
    class StatusChoices(models.TextChoices):
        DONE = "DONE", "Done"
        PROCESSING = "PROCESSING", "Processing"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to="pdf_files")
    status = models.CharField(max_length=24, default=StatusChoices.PROCESSING)


class PDFImages(models.Model):
    image = models.ImageField(upload_to="pdf_images")
    number = models.IntegerField(default=0)
    file = models.ForeignKey("File", on_delete=models.CASCADE)
