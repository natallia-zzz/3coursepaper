from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/model1', views.model1, name='model1'),
    path('/model2', views.model2, name='model2'),
    path('/model3', views.model3, name='model3'),
]
