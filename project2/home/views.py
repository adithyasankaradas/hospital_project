from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors,Booking
# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def department(request):
    dict_dept={
'dept':Departments.objects.all()
}
    return render(request,'department.html',dict_dept)
def contact(request):
    return render(request,'contacts.html')
def doctors(request):
 dict_doc = {
'doc' :Doctors.objects.all()
}
 return render(request,'doctors.html',dict_doc)
def booking(request):
    return render(request,'bookings.html')
from .forms import BookingForm
def booking(request):
 form = BookingForm()
 dict_form ={
'form': form
}
 return render(request,'bookings.html', dict_form)
