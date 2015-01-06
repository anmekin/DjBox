__author__ = 'andrey'
# -*- coding: utf-8 -*-
from django.forms import forms, CharField, ModelForm

from handlers import upload_to_dropbox
from models import DropObjet

class UploadFileForm(ModelForm):
    class Meta:
        model = DropObjet
        fields=[]
    #title = CharField(max_length=50)
    file = forms.FileField()

    def my_save(self, request):
        f = self.cleaned_data['file']
        path = '/'+request.user.username+'/'+f.name
        print 'Upload path:', path
        tmp = upload_to_dropbox(path, f)
        print 'Returned by dropbox:', tmp
        self.instance.name = tmp.split('/')[-1].replace(' ', '_')
        print 'Object name:', self.instance.name
        self.instance.user = request.user
        print 'User name:' , self.instance.user
        obj = super(UploadFileForm, self).save()
        return obj

    # def save(self, commit=False):
    #     f = self.cleaned_data['file']
    #     #obj = super(UploadFileForm, self).save(commit=False)#
    #     path = upload_to_dropbox(f)
    #     self.instance.
    #     obj = super(UploadFileForm, self).save()
    #     return obj
        # fileModel = new FileModel(path)

