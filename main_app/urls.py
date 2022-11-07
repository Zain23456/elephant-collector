from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('elephants/', views.elephants_index, name='elephants_index'),
  path('elephants/<int:elephant_id>/', views.elephants_detail, name='elephants_detail')

]