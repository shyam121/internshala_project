
from documentapp.models import *
from db_file_storage.form_widgets import DBClearableFileInput

from django import forms

class DocumentForm(forms.ModelForm):
    class Meta(object):
        model=Document
        exclude=['user']
        widgets={
            'marksmemo':DBClearableFileInput,
        }

class SingleDocumentForm(forms.ModelForm):
    class Meta(object):
        model=SingleDocument
        exclude=['user']
        widgets={
            'file':DBClearableFileInput,
        }