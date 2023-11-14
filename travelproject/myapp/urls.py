
from django.urls import path, include

from myapp import views

urlpatterns = [
   path('register/',views.second,name='myapp'),
   path('login',views.login,name='login'),
   path('logout',views.logout,name='logout'),

]