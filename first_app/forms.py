from django.contrib.auth.forms import UserCreationForm
from django import forms
from .constant import  GENDER_TYPE
from django.contrib.auth.models import User
# from .models import UserBankAccount, userAddress

class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField( choices=GENDER_TYPE)
    city = forms.CharField(max_length=100)
    country = forms.CharField(max_length = 100)
    
    
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        
    def save(self, commit = True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()
            # account_type = self.cleaned_data.get('account_type')
            
            
            # street_address = self.cleaned_data.get('street_address')
            
            # userAddress.objects.create(
            #     user = our_user,
            #     street_address= street_address,
            #     city = city,
            #     postal_code = postal_code,
            #     country = country
            # )
            
            # UserBankAccount.objects.create(
            #     User = our_user,
            #     account_type= account_type,
            #     birth_date = birth_date,
            #     gender = gender
            # )
        return our_user
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for filed in self.fields:
            self.fields[filed].widget.attrs.update({
                'class':'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
            })
            
class UserUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    city = forms.CharField(max_length= 100)
    country = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })