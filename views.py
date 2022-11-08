from django.shortcuts import render
from django.contrib import messages , auth
from django.contrib.auth.models import User
from django.shortcuts import render , redirect

# Create your views her

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate ( username = username , password = password )
        if user is not None:
            auth.login ( request , user )
            return redirect ( '/' )
        else:
            messages.info ( request , 'invalid details' )
            return redirect ( '/' )
    else:
        return render ( request , "login.html" )


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method=='POST':
        username = request.POST['username']
        password1= request.POST['password1']
        password2 = request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email)
                user.save();
                print("User created")
                return redirect ( '/' )


        else:
            print("passowrd not matched")
            return redirect('/')
    else:
        return render(request,'register.html')

def about(request):

    return render(request, 'about.html')






