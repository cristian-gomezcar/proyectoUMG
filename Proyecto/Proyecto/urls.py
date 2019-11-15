"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,include
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('App1/', include(('Apps.App1.urls','app1'), namespace='app1')),  
    path('App2/', include(('Apps.App2.urls','app1'), namespace='app2')),  
    path('accounts/login/', LoginView.as_view(template_name='Usuario/logiarse.html'),name = 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    #path('reset/passwordReset', PasswordResetView, {'template_name : registration/password_reset_form.html','email_template_name:registration/password_reset_email.html'}, name = 'passwordReset'),
    #path('reset/passwordResetDone', PasswordResetDoneView, {'template_name : registration/password_reset_done.html'}, name='passwordResetDone'),
    #path('reset/<uidb64>/<token>',PasswordResetConfirmView, {'template_name : registration/password_reset_confirm.html'}, name='passwordResetConfirm'),
    #path('reset/done', PasswordResetCompleteView, {'template_name : registration/password_reset_complete.html'}, name='PasswordResetComplete'),
    
]

