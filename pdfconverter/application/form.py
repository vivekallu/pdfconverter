from django import forms

class UploadFileForm(forms.Form):
    url = forms.URLField(max_length=500)
    file  = forms.FileField(required=False)
