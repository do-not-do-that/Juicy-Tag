from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'juicy_main'

urlpatterns=[
    url(r'^$', views.Juicy_main.as_view(), name='juicy_main'),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)