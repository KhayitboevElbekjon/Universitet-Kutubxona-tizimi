from django import forms
from  .models import *
class TalabaForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=30,label='Ism')
    course = forms.IntegerField(min_value=1, max_value=7,label='Kurs')
    books = forms.IntegerField(min_value=0, max_value=10,label='Kitob soni')
    graduate = forms.BooleanField(label='Bitiruvchi',required=False)

class MuallifForm(forms.Form):
    ism=forms.CharField(max_length=25)
    tirik=forms.BooleanField()
    kitoblar_soni=forms.IntegerField()
    jinsi=forms.CharField(max_length=10)
    yosh=forms.IntegerField()

class KitobForm(forms.ModelForm):
    class Meta:
        model=Kitob
        fields=('nom','sahifa','janr','mualif_fk')  # ('__all__')

class RecordForm(forms.ModelForm):
    class Meta:
        model=Record
        fields=('__all__')

class AdminForm(forms.Form):
    ism=forms.CharField(max_length=25,label='Ism:')
    ish_vaqti=forms.TimeField(label='Ish vaqti:')