from django.urls import path
from . import views
from django.urls import path, include
from .views import TerapeutaPacientesView





urlpatterns = [
    # Profile
    path("usuario/", views.UsuarioView.as_view(), name="terapeuta"),
    path("usuario/<str:pk>/", views.UsuarioDetail.as_view(), name="paciente"),
path('terapeuta/<int:pk>/pacientes/', TerapeutaPacientesView.as_view(), name='terapeuta-pacientes'),



]
