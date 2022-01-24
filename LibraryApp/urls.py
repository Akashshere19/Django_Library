from django.contrib import admin
from django.urls import path,include
from LibraryApp import views
urlpatterns=[
    path('', views.add_book, name='home'),

    path('delete/<int:id>/', views.delete_data, name='delete'),
    path('<int:id>/', views.update_data, name='update'),
]
