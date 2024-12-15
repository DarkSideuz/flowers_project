from django.urls import path
from . import views

urlpatterns = [
    path('', views.flower_list, name='flower_list'),
    path('type/<int:type_id>/', views.flowers_by_type, name='flowers_by_type'),
    path('flower/<int:flower_id>/', views.flower_detail, name='flower_detail'),
]