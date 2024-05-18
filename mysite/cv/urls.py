from django.urls import path
from . import views

urlpatterns = [
    path('', views.Students.as_view(), name='students'),
    path('<int:pk>/', views.information.as_view(), name='information'),
    path('new/', views.ProfileView.as_view(), name='new_student'),
    path('<int:pk>/edit/', views.ProfileUpdate.as_view(), name='edit'),
    path('<int:pk>/delete/', views.ProfileDelete.as_view(), name='delete'),
]