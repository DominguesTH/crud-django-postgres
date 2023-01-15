from django.urls import path
from .views import listagem, nova_transacao, update, delete


urlpatterns = [
    path('', listagem , name='url_listagem' ),  
    path('nova/', nova_transacao , name='url_nova' ),  
    path('update/<int:pk>/', update, name='url_update'),
    path('delete/<int:pk>/', delete, name='url_delete'),
]