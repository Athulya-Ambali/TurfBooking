from django import forms
from turfapp.models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['turf','name','email','contact','sport','slot','hour','players','book_date']
        widgets = {
            'book_date': forms.DateInput(attrs={'type': 'date'}),
            
        }
