from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model, logout
from User.forms import LoginForm, RegisterForm


def login_page(request):
    if request.user.is_authenticated():
        return redirect("/")
    form = LoginForm()
    if form.is_valid():
        User = get_user_model()
        email = form.cleaned_data.get("email")
        try:
            username = User.objects.get(email=email.lower()).username
            print(username)
        except:
            username = None
            print("wrong")
        print(email)
        password = form.cleaned_data.get("password")
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("/")
    return render(request, "auth/login.html", {"content": form})


def register_page(request):
    if request.user.is_authenticated():
        return redirect("/")
    User = get_user_model()
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        new_user = User.objects.create_user(username, email, password)
        if new_user is not None:
            login(request, new_user)
            return redirect("/")
    return render(request, "auth/register.html", {"form": form})


def logout_page(request):
    logout(request)
    return redirect("/")
