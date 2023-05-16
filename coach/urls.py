from django.urls import path
from .import views
app_name='coach'
urlpatterns=[
path('home',views.home,name='home'),
path('indexcoach',views.indexcoach,name='indexcoach'),

]