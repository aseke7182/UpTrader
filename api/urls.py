from django.urls import path
from .views import ping, list_menu_render

urlpatterns = [
    path('ping', ping),
    path('menu_render', list_menu_render, name='menu'),
    path('menu_render/<str:name>', list_menu_render, name='menu_detail')
]
