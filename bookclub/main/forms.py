from django.forms import ModelForm
from .models import *

class BookForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'title',
            'author',
            'genre',
            'pages',
            'room'
    ]