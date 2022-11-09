from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('elephants/', views.elephants_index, name='elephants_index'),
  path('elephants/<int:elephant_id>/', views.elephants_detail, name='elephants_detail'),
  path('elephants/create/', views.ElephantCreate.as_view(), name='elephants_create'),
  path('elephants/<int:pk>/update/', views.ElephantUpdate.as_view(), name='elephants_update'),
  path('elephants/<int:pk>/delete/', views.ElephantDelete.as_view(), name='elephants_delete'),
  path('elephants/<int:elephant_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('elephants/<int:elephant_id>/assoc_toy/<int:toy_id>', views.assoc_toy, name='assoc_toy'),
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  path('toys/', views.ToyList.as_view(), name='toys_index'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]