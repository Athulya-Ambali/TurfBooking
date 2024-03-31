from django.shortcuts import render,redirect
from turfapp.models import Sport
from turfapp.models import Turf
from turfapp.models import Booking
from turfapp.models import Slot
from turfapp.models import Hour
from userapp.forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

@login_required
def home(request):
    if request.user.is_authenticated:
        return render(request, 'turfuser/layout/index.html')
    else:
        return render(request, 'login.html')



def loginview(request):
    uname = request.POST['username']
    pwd = request.POST['password']
    user = authenticate(request, username=uname, password=pwd)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return render(request,"login.html")
        
def logout_view(request):
    logout(request)
    return redirect('login')


def sign_up(request):
        uform = UserCreationForm(request.POST)
        if request.method == "POST":
            if uform.is_valid():
                uname = uform.cleaned_data.get('username')
                pwd = uform.cleaned_data.get('password1')
                email=uform.cleaned_data.get('email')
                user1=User.objects.create_user(username=uname,password=pwd,email=email)
                user1.save()
                user1 = authenticate(request, username=uname, password=pwd)
                login(request,user1)
                return redirect('home')
        else:
            uform = UserCreationForm()
        return render(request, 'registration/sign_up.html', {'form': uform})
    
# def Resethome(request):
#     return render(request,'registration/ResetPassword.html')

# def resetPassword(request):
#     responseDic={}
#     try:
#         usern = request.POST['uname']
#         recepient=request.POST['email']
#         pwd=request.POST['password']
#         #subject="Password reset"
#         try:
#             user=User.objects.get(username=usern)
#             if user is not None:
#                 user.set_password(pwd)
#                 user.save()
#                 #send_mail(subject,message, EMAIL_HOST_USER, [recepient])
#                 responseDic["errmsg"]="Password Reset Successfully"
#                 return render(request,"registration/ResetPassword.html",responseDic)
#         except Exception as e:
#             print(e)
#             responseDic["errmsg"]="Email doesnt exist"
#             return render(request,"registration/ResetPassword.html",responseDic)
        
#     except Exception as e:
#         print(e)
#         responseDic["errmsg"]="Failed to reset password"
#         return render(request,"registration/ResetPassword.html",responseDic)





def sportview(request):
    obj=Sport.objects.all()
    return render(request,'turfuser/sportview.html',{'data':obj})

def turfview(request):
    obj=Turf.objects.all()
    return render(request,'turfuser/turfview.html',{'data':obj})

def slotview(request):
    obj=Slot.objects.all()
    return render(request,'turfuser/slotview.html',{'data':obj})

def hourview(request):
    obj=Hour.objects.all()
    return render(request,'turfuser/hourview.html',{'data':obj})

def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('bookview')
    else:
        form = BookingForm()
    return render(request,'turfuser/booking.html',{'form':form})

def bookview(request):
    obj=Booking.objects.all()
    return render(request,'turfuser/bookingview.html',{'data':obj})

def index(request):
    return render(request,'turfuser/layout/index.html')



