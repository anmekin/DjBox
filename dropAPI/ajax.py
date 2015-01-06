__author__ = 'andrey'

from django.shortcuts import render, Http404
from models import DropObjet
from django.conf import settings
import dropbox

def userfiles_ajax(request):
    print "user: ", request.user
    if request.is_ajax():
        client = dropbox.client.DropboxClient(settings.AUTH_TOKEN)
        #print request.user
        #metadata = client.metadata("/" + request.user.username)
        delta = client.delta(path_prefix="/" + request.user.username)
        # metadata = client.metadata("/admin")
        files = []
        for file in delta['entries'][1:]:
            #print file[0].split('/')[-1]
            files.append(file[0].split('/')[-1]) # remove slash
        return render(request, 'userfiles_ajax.html', {'files': files})
    else:
        raise Http404('IS NOT AJAX')