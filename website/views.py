from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .form import SignUpForm

# Create your views here.
def home(request):
    #check user 
    if request.method=="POST":
       username=request.POST['username']
       password=request.POST['password']
       user=authenticate(request,username=username,password=password)
       if user !=None:
           login(request,user)
           messages.success(request,"you have loged success")
           return redirect('home')
       else:
           messages.success(request,"sorry there somthing bad hapen please try againe ..")
           return redirect('home')
    else:
        return render(request,"home.html",{})

def logout_user(request):
     logout(request)
     messages.success(request,"see you later !")
     return redirect('home')

def register_user(request):
      if request.method=="POST":
          form = SignUpForm(request.POST)
          if form.is_valid():
              form.save()
              username=form.cleaned_data['username']
              password=form.cleaned_data['password1']

              user =authenticate(request,username=username,password=password)
              login(request, user)
              messages.success(request, "You Have Successfully Registered! Welcome!")
              return redirect('home')
      else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})  
      
      return render(request, 'register.html', {'form':form}) 


