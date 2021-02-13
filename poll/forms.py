from django.forms import ModelForm

from .models import Poll
from .models import Comment

from django import forms

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three', 'option_four', 'option_five','additionalnotes']
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','AreYouVoting','email','note']
