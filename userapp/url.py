from django.urls import path
from userapp import views

urlpatterns = [

    path('sportview/',views.sportview,name="sports"),
    path('turfview/',views.turfview,name="turf"),
    path('slotview/',views.slotview,name="slot"),
    path('hourview/',views.hourview,name="hour"),
    path('bookview/',views.bookview,name="bookview"),
    path('bookform/',views.book,name="bookform"),
    path('',views.home,name='home'),
    path('accounts/login/',views.loginview,name="login"),
    path('logout',views.logout_view),
    path('accounts/sign_up/',views.sign_up,name="signup"),
    # path('reset/',views.Resethome,name="reset"),
    # path('passwordreset/',views.resetPassword,name="passwordreset"),
    path('index/',views.index,name="index"),
 

  
    
    
]
