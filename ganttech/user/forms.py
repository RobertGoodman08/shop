from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput

from user.models import UserProfile


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    last_name = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'password1', 'password2', )




class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ( 'username','email','first_name','last_name')
        widgets = {
            'username': TextInput(attrs={'class': 'input','placeholder':'username'}),
            'email': EmailInput(attrs={'class': 'input','placeholder':'email'}),
            'first_name': TextInput(attrs={'class': 'input','placeholder':'first_name'}),
            'last_name': TextInput(attrs={'class': 'input','placeholder':'last_name' }),
        }

CITY = [
    ('Ашхабад', 'Ашхабад'),
    ('Аннау', 'Аннау'),
    ('Балканабад', 'Балканабад'),
    ('Дашогуз', 'Дашогуз'),
    ('Мары', 'Мары'),
    ('Туркменабад', 'Туркменабад'),
]
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city','country','image')
        widgets = {
            'phone': TextInput(attrs={'class': 'input','placeholder':'phone'}),
            'address': TextInput(attrs={'class': 'input','placeholder':'address'}),
            'city': Select(attrs={'class': 'input','placeholder':'city'},choices=CITY),
            'country': TextInput(attrs={'class': 'input','placeholder':'country' }),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image', }),
        }