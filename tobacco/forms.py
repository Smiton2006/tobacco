from django.forms import  ModelForm
from models import Tobacco

class TobaccoForm(ModelForm):
    class Meta:
        model = Tobacco
        fields = ['brand','taste_kind','taste', 'img_src']