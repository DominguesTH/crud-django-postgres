from django.urls import path
from .views import home


urlpatterns = [
    path('', home , name='url_home' ), 
    # path('horario/', horario, name='url_horario' ),     
]