
from django.urls import path,include
from .views import Delete_Task, homepage,addtodo

urlpatterns = [
    path('',homepage,name='home'),
    path('add',addtodo,name='addtodo'),
    path('add/<int:id>',Delete_Task,name='deletetodo'),
]
