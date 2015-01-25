#coding:utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, render, redirect
from forms import UploadFileForm

def home(request):
    form = UploadFileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.my_save(request)
        return redirect('/')
    else:
        return render(request, "index.html", {"form": form})

# @login_required()
# def userfiles(request):
#     files = DropObjet.objects.filter(user=request.user)
#     #files = DropObjet.objects.all()
#     for file in files:
#         print file.name
#     return render(request, "userfiles.html", {'files': files})
#
# @login_required()
# def show_file(request):
#     name = request.GET.get('name')
#     #name = name.replace('_', ' ')
#     print name
#     print 'Good'
#     file = get_object_or_404(DropObjet, name=name, user=request.user)
#     client = dropbox.client.DropboxClient(settings.AUTH_TOKEN)
#     shared_url = client.share(file.get_path(), short_url=True)
#     print shared_url['url']
#     return render(request, "show_file.html", {'link': shared_url['url']})