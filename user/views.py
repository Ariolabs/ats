from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import UserRegisterForm
# Create your views here.
User = get_user_model()
def index(request):
    user = request.user
    token = user.generate_token()
    print(token.key)
    return render(request, 'user/index.html',context={"token": token})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "user/register.html", {"form": form})

def get_tocken(request):
    ...