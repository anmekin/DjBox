#coding:utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render_to_response, render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from forms import UploadFileForm
from models import DropObjet
from django.conf import settings
import dropbox


def loadToDropBox(request):
    APP_KEY = 'q860zezp5zss55a'
    APP_SECRET = '0ekwbpg9czsu8l9'
    flow = dropbox.client.DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)
    authorize_url = flow.start()
    code = raw_input("Enter the authorization code here: ").strip() # WTF?
    access_token, user_id = flow.finish(code)
    client = dropbox.client.DropboxClient(access_token)
    f = open('working-draft.txt', 'rb')
    response = client.put_file('/magnum-opus.txt', f)
    print "uploaded:", response
    return render(request, 'index.html')
# Create your views here.

# def upload(request):
#     form = UploadFileForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
# #        print request.FILES
#         obj = form.my_save(request)
#         print obj.get_path()
#         #handle_uploaded_file(request.FILES['file'])
#         return redirect('/')
#     else:
#         return render(request, "index.html", {"form": form})


def home(request):
    form = UploadFileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
#        print request.FILES
        obj = form.my_save(request)
        #print obj.get_path()
        #handle_uploaded_file(request.FILES['file'])
        return redirect('/')
    else:
        return render(request, "index.html", {"form": form})

@login_required()
def userfiles(request):
    files = DropObjet.objects.filter(user=request.user)
    #files = DropObjet.objects.all()
    for file in files:
        print file.name
    return render(request, "userfiles.html", {'files': files})

@login_required()
def show_file(request):
    name = request.GET.get('name')
    #name = name.replace('_', ' ')
    print name
    print 'Good'
    file = get_object_or_404(DropObjet, name=name, user=request.user) # в будующем формировка пути с учетом текущего пользователя
    client = dropbox.client.DropboxClient(settings.AUTH_TOKEN)
    shared_url = client.share(file.get_path(), short_url=True)
    print shared_url['url']
    return render(request, "show_file.html", {'link': shared_url['url']})