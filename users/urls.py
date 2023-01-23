from django.urls import path
from .views import login, cadastro,logout


urlpatterns = [
    path('', login, name='url_login'),
    path('cadastro/', cadastro, name='url_cadastro'),
    path('logout/', logout, name='url_logout'),
]