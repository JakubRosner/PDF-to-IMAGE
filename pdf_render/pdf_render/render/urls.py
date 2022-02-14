from django.urls import path
from .views import(
    CreateFile,
    RetrieveFile,
    RetrieveImage,
)

urlpatterns = [
    path("documents/", CreateFile.as_view()),
    path("documents/<uuid:id>/", RetrieveFile.as_view()),
    path("documents/<uuid:file_id>/pages/<int:number>/", RetrieveImage.as_view()),
]
