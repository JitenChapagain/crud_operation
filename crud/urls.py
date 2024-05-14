from django.contrib import admin
from django.urls import path
from crud.views import *

urlpatterns = [
    path('', index, name='index'),
    path('add',add, name='add'),
    path('edit',edit, name='edit'),
    path('update/<str:id>',update, name='update'),
    path('delete/<str:id>', delete, name="delete")
]
