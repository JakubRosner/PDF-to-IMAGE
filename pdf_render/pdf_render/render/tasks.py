from celery import task
from pdf2image import convert_from_path
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
from .models import PDFImages, File
import os

IMAGE_PATH = "/tmp/pdf_images/"
SIZE = (1200, 1600)


@task
def proces_pdf(file_id):
    number = 1
    file = File.objects.get(id=file_id)

    # checking for IMAGE_PATH Dir
    if not os.path.exists(IMAGE_PATH):
        os.makedirs(IMAGE_PATH)

    # Pdf to PIL image conversion
    images = convert_from_path(
        pdf_path=f'/tmp/{file.file.name}',
        dpi=200,
        size=SIZE,
    )

    # Saving and convering PIL images
    to_create = []
    for image in images:
        image_name = f'image{number}.jpg'
        image.save(f'{IMAGE_PATH}{image_name}', 'JPEG')
        img = Image.open(f'{IMAGE_PATH}{image_name}')
        img.thumbnail(SIZE, Image.ANTIALIAS)
        thumb_io = BytesIO()
        img.save(thumb_io, img.format, quality=200)
        content = ContentFile(thumb_io.getvalue(), f'tmp/{image_name}')
        to_create.append(PDFImages(file=file, number=number, image=content))

        number += 1

    PDFImages.objects.bulk_create(to_create)

    # Updating status on File object
    file.status = File.StatusChoices.DONE
    file.save()
