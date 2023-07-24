from django import forms
from .models import *
class GradeForm(forms.ModelForm):
    
    class Meta:
        model = Grade
        fields = ("__all__")


class ResponsableForm(forms.ModelForm):
    """Form definition for Responsable."""

    class Meta:
        """Meta definition for Responsableform."""

        model = Responsable
        fields = ('__all__')
        widgets = {
            'Image':forms.TextInput(
                attrs = {
                    'type':'file'
                }
            )
        }


from ckeditor.widgets import CKEditorWidget
from django import forms

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'