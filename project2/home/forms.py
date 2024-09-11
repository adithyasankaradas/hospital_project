from django import forms
from .models import Booking
class BookingForm(forms.ModelForm):
 class Meta:
  model = Booking
  fields = '__all__'
from django import forms
from .models import Booking
class DateInput(forms.DateInput):
 input_type = 'date'
class BookingForm(forms.ModelForm):

 class Meta:
  model = Booking
  fields = '__all__'
  widgets={

  'booking_date':DateInput()
}
  labels={
   'p_name':"Patient name",
   'p_phone':"Patient phone",
   'p_email':"patient email",
   'doc_name':"Doctor name",
   'Booking_date':"Date"

  }