from django.contrib import auth
from django.shortcuts import render_to_response, redirect, render
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "User not found"
            return render(request, "login.html", args)
    else:
        return render(request, "login.html", args)

def logout(request):
    auth.logout(request)
    return redirect("/")

def signup(request):
    args = {}
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
            args['form'] = newuser_form
    return render(request, 'signup.html', args)

# def get_profile(user):
#                 profile, created = UserProfile.objects.get_or_create(user=user)
#                 return profile
