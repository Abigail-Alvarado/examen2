
from django.contrib import admin
from django.urls import path #import    amos todas las clases de las vistas
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orden/',OrdenesView.as_view(), name='Orden_list'),
     path('orden/<int:id>',OrdenesView.as_view(), name='Orden_list'),
    
    
 

    
]
