from django import forms
from pawsitting.models import *
from django.forms import ModelForm
from pawsitting.models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'start_date', 'end_date']
        widgets = {
            'service': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        }
    def __init__(self, *args, **kwargs):
         # สร้างฟอร์มตามปกติ
        sitter = kwargs.pop('sitter', None)
        super().__init__(*args, **kwargs)
        # ถ้ามี sitter ส่งเข้ามา
        if sitter:
            # ลองหาข้อมูลโปรไฟล์ของ sitter
            try:
                profile = SitterProfile.objects.get(user=sitter)
                self.fields['service'].queryset = profile.service.all() # แสดงเฉพาะบริการที่ sitter คนนั้นมีในโปรไฟล์
            except SitterProfile.DoesNotExist:
                self.fields['service'].queryset = Service.objects.none()