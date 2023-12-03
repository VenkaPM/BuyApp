from django.urls import path

from buyapp.buyer import views

urlpatterns = (
    path('', views.index, name='index'),
    path('info/', views.info, name='info'),
)
