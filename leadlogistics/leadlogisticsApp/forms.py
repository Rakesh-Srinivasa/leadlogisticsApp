from django import forms
from django.contrib.auth.models import User
from leadlogisticsApp.models import Docket,Contact
from django.contrib import admin

class DocketForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = Docket
        fields = ('DocketId',)

    def clean_asset_code(self):
            DocketId = self.cleaned_data['DocketId']
            if Docket.objects.filter(DocketId=DocketId).exists():
                raise forms.ValidationError("This Docket entry already exist.")
            return DocketId

class DocketAdmin(admin.ModelAdmin):
    form = DocketForm



class ContactUsForm(forms.ModelForm):
    class Meta():
        model = Contact
        fields = '__all__'
