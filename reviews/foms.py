from pyexpat import model
from django import forms
from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "subtitle",
            "content",
        ]
