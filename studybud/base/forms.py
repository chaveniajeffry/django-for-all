from django.forms import ModelForm
from .models import Room, User
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username','password1','password2']
class RoomForm(ModelForm):
    class Meta:
        model = Room
        # Will have an input in all fields of model
        fields = '__all__'
        exclude = ['host','participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        # Will have an input in all fields of model
        fields = ['avatar','name','username','email','bio']