from django import forms
from .models import Topic, Post


class TopicForm(forms.ModelForm):
    message = forms.CharField()

    class Meta:
        model = Topic
        fields = {'subject', 'message'}


        


    
