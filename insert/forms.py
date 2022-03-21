from django import forms  
from insert.models import Products 


class Prdct(forms.ModelForm):  
    class Meta:  
        model = Products  
        fields = '__all__'  