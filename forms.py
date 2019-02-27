from django.forms import ModelForm, Form
from django import forms
from lid.models import ModelSuggestion

class ModelSuggestionForm(ModelForm):
    class Meta:
        model = ModelSuggestion
        fields = ['model_name', 'model_source', 'source_link', 'model_text', 'your_name', 'your_email']

class ModelAddingForm(Form):
    model_type_id = forms.IntegerField(label='Model type ID number')
    category_id = forms.IntegerField(label='Category ID number')
    subject_id = forms.IntegerField(label="Subject ID number")
    description_id = forms.IntegerField(label="Description ID number.")
    model_name = forms.CharField(label="Name for the model", max_length=200) 
    source_link = forms.CharField(label="URL for the source of the model", max_length=350) 
    model_legislation_source = forms.CharField(label="Name of the model source", max_length=200) 
    model_legislation_text = forms.CharField(label="Text of the model itself", widget=forms.Textarea)
