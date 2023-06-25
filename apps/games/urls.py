from django.urls import path

#Local
from .views import index, random, about, round,test_render, main_page


urlpatterns = [
    path('main/', index),
    path('main/random', random),
    path('main/about', about),
    path('main/moveround', round),
    path('render/', test_render),
    path('render/mainpage', main_page)
]