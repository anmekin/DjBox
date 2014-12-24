__author__ = 'andrey'

from django.shortcuts import render, Http404
from models import DropObjet

def userfiles_ajax(request):
    print "user: ", request.user
    if request.is_ajax():
        return render(request, 'userfiles_ajax.html', {'files': DropObjet.objects.filter(user=request.user)})
    else:
        raise Http404('IS NOT AJAX')