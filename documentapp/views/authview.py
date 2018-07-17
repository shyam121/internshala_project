from django.views import View
from django.views.generic import ListView
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from documentapp.forms import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

class SignupView(View):
    def get(self,request):
        signupform=SignupDETAILS()
        return render(request=request,template_name="authtemplates/signup.html",context={"form":signupform})
    def post(self,request):
        form=SignupDETAILS(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            user=authenticate(request,username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                return redirect("documentapp:singledoc.list")
            else:
                return redirect("documentapp:sign_up")

class LoginView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('documentapp:singledoc.list')
        loginform=LoginupDETAILS()
        return render(request=request,template_name="authtemplates/loginpage.html",context={"form":loginform})

    def post(self,request):
        form=LoginupDETAILS(request.POST)
        if form.is_valid():
            user=authenticate(request,username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                return redirect("documentapp:singledoc.list")
            else:
                return redirect("documentapp:loginpage")

def logout_user(request):
    logout(request)
    return redirect("documentapp:loginpage")
