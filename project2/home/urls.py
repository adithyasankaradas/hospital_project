
from django.urls import path,include
from.import views
urlpatterns = [
   
    path('', views.index,name='index'),
    
    path('about',views.department,name='about'),
    path('contact',views.contact,name='contact'),
    path('doctors',views.doctors,name='doctors'),
    path('booking',views.booking,name='booking')
    
]
