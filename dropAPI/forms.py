__author__ = 'andrey'
# -*- coding: utf-8 -*-

from handlers import upload_to_dropbox
from django import forms

class UploadFileForm(forms.Form):
    # class Meta:
    #     model = DropObjet
    #     fields=[]
    file = forms.FileField()

    def my_save(self, request):
        f = self.cleaned_data['file']
        path = '/'+request.user.username+'/'+f.name
        upload_to_dropbox(path, f)