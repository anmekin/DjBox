__author__ = 'andrey'

from django.shortcuts import render, Http404, HttpResponse
import dropbox
from django.conf import settings

def userfiles_ajax(request):
    if request.is_ajax():
        client = dropbox.client.DropboxClient(settings.AUTH_TOKEN)
        delta = client.delta(path_prefix="/" + request.user.username)
        files = []
        for file in delta['entries']:
            name = file[0].split('/')[-1]
            if name != request.user.username:
                files.append(name)
        return render(request, 'userfiles_ajax.html', {'files': files})
    else:
        raise Http404('IS NOT AJAX')

def show_file_ajax(request):
    name = request.GET.get('name')
    client = dropbox.client.DropboxClient(settings.AUTH_TOKEN)
    path = '/' + request.user.username + '/' + name
    shared_url = client.share(path, short_url=True)
    return HttpResponse(shared_url['url'])

def delete_file_ajax(request):
    name = request.GET.get('name')
    client = dropbox.client.DropboxClient(settings.AUTH_TOKEN)
    path = '/' + request.user.username + '/' + name
    client.file_delete(path)
    print path
    return HttpResponse("OK")