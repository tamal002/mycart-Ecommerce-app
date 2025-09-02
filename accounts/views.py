from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from django.contrib import messages


# login logic

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("shop:index")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("accounts:login")
            
        
    return render(request, 'accounts/login.html')




# register logic



def register_view(request):
    User = get_user_model()
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # re-checking the "password" and "confirm_password"
        if password != confirm_password:
            messages.error(request, "error: password not matched")
            return redirect("accounts:register")

        # checking any user with same username already exists or not
        if User.objects.filter(username=username).exists():
            messages.error(request, "error: username already exists")
            return redirect("accounts:register")
    
        # creating the user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        login(request, user)
        return redirect("accounts:login")

    return render(request, 'accounts/register.html')