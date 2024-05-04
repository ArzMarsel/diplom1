from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.List_of_dishes.as_view(), name='Dishes')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)