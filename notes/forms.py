from django import forms
from .models import Notes
 
 
# creating a form
class NotesForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Notes
 
        # specify fields to be used
        fields = [
            "title",
            "description",
            "Query"
        ]