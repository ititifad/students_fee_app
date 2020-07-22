from django .forms import ModelForm
from .models import Records
from django import forms

class RecordsForm(forms.ModelForm):
    class Meta:
        model = Records
        fields = ['students','classrooms','school_fees','received_fees','Remaining_fees', 'phone_number', 'completed']