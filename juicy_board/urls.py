from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'juicy_board'

urlpatterns = [
    url(r'^$', views.Juicy_board.as_view(), name='juicy_board'),
    url(r'^insert/$', views.check_post, name="juicy_board_insert"),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.Juicy_board_detail.as_view(), name="juicy_board_detail"),
    url(r'^(?P<pk>[0-9]+)/update/$', views.Juicy_board_update.as_view(), name="juicy_board_update"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)