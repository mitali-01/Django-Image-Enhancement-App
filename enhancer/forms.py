from django import forms

class CustomEnhancementForm(forms.Form):
    sharpness = forms.FloatField(label='Sharpness', initial=4.0, min_value=0.1, max_value=10.0)
    contrast = forms.FloatField(label='Contrast', initial=1.3, min_value=0.1, max_value=5.0)
    blur = forms.IntegerField(label='Blur', initial=3, min_value=1, max_value=10)

class ImageUploadForm(forms.Form):
    image = forms.ImageField(label="Upload Image")