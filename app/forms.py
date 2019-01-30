from django.forms import ModelForm
from app.models import Monent

class MomentForm(ModelForm):
    class meta:
        model = Monent
        fields = '__all__'
