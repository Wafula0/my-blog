from django.urls import path
from. import views

urlpatterns= [
    path('',views.index,name='index'),
    path('Post/<int:pk>', views.Post, name='Post'),
]