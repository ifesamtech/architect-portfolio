from django import forms
from . models import Cv, ContactMessage, Project, Category
# from ckeditor.widgets import CKEditorWidget


class CvForm(forms.ModelForm):
    class Meta:
        model = Cv
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'subject', 'message']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'category', 'image', 'description']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'