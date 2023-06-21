from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from UserAuth.forms import CreateUserForm
from django.contrib import messages


# Create your views here.


def signup(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')            
            password = form.cleaned_data.get('password1')            
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect(home)
        else:
            print(form.errors)
            return render(request,"UserAuthTemplates/autherror.html")

    else:
        form = CreateUserForm()
        return render(request,"UserAuthTemplates/signup.html",{'form':form})


def home(request,username):
    return render(request,"Homepage/home.html",{'user':request.user})   



# user Signin (Request):

def signin(request):
    if request.user.is_authenticated:
        username = request.user.get_username()
        username = request.user.get_username()
        return redirect(home,username)
     
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            username = request.user.get_username()
            return redirect(home,username)
        
        else:
            messages.info(request,"Error loging in, please try again")
            form = AuthenticationForm()
            return render(request,"UserAuthTemplates/signin.html",{'form':form})
    else:
        form = AuthenticationForm()
        return render(request,"UserAuthTemplates/signin.html",{'form':form})


# def signout(request):

def signout(request):
    logout(request)
    return redirect(signin)