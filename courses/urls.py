"""codewithabhishek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from courses.views import coursePage, SignupView, LoginView , signout , checkout, verifyPayment , MyCoursesList , HomePageView , SearchView, ProfileList #importin home function  from course folder 
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from codewithabhishek.settings import MEDIA_ROOT, MEDIA_URL

    

urlpatterns = [
    path('',HomePageView.as_view(), name = 'home' ),
    path('logout',signout, name = 'logout' ),
    path('signup',SignupView.as_view(), name = 'signup' ),
    path('login',LoginView.as_view(), name = 'login' ),
    path('course/<str:slug>',coursePage, name = 'coursepage' ),
    path('check-out/<str:slug>',checkout, name = 'checkout' ),
    path('verify_payment',verifyPayment, name = 'verify_payment' ),
    path('profile',ProfileList.as_view(), name = 'profile' ),
    path('my-courses', MyCoursesList.as_view(), name = 'my-courses' ),
    path('search',SearchView.as_view(), name = 'search' ),
    

    #url for password reset and password change

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "courses/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "courses/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "courses/password_reset_form.html"), name= "password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "courses/password_reset_done.html"), name="password_reset_complete"),
    
    #end of custom url for password reset anc chang e
    
    
    
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
