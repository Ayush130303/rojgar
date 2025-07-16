from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name='logout'),
    path('add_profile/<int:jobid>/',views.add_profile,name='add_profile'),
    path('profile/',views.profile,name='profile'),
    path('delete_job/<int:id>/',views.delete_job,name='delete_job'),

]
