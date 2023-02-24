from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        # Will have an input in all fields of model
        fields = '__all__'
        exclude = ['host','participants']