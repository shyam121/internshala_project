from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from documentapp.models import *
from documentapp.forms import *
from django import urls

from django.contrib.auth.models import User

class show_profile(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model=Profile
    template_name = 'authtemplates/profilepage.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(show_profile, self).get_context_data(**kwargs)
        context['obj'] = Profile.objects.get(pk=self.kwargs['pk'])
        context['user']=User.objects.get(pk=self.kwargs['pk'])
        context['personid'] = self.request.user.id
        return context

class UserDetailsView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    queryset=Profile.objects.all()
    template_name = 'authtemplates/userdetails.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserDetailsView, self).get_context_data(**kwargs)
        context['userid'] = self.request.user.id
        return context

class add_profile(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = Profile
    form_class = ProfileForm
    template_name = 'profiletemplates/profile_add.html'
    success_url = urls.reverse_lazy('documentapp:singledoc.list')

    def post(self, request, *args, **kwargs):
        username = self.request.user.get_username()
        credit_form = ProfileForm(request.POST, request.FILES, initial={'user': request.user})
        if credit_form.is_valid():
            credit_card = credit_form.save(commit=False)
            credit_card.user = self.request.user
            credit_card.save()
            return redirect('documentapp:singledoc.list')
        else:
            return redirect('documentapp:loginpage')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(add_profile, self).get_context_data(**kwargs)
        context['userid'] = self.request.user.id
        return context

class edit_profile(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url = '/login/'
    model = Profile
    form_class = ProfileForm
    template_name = 'profiletemplates/profile_update.html'

    success_url = urls.reverse_lazy('documentapp:singledoc.list')
    def has_permission(self):
        existing_form = Profile.objects.get(pk=self.kwargs['pk'])
        if self.request.user == existing_form.user:
            return True
        else:
            PermissionError
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(edit_profile, self).get_context_data(**kwargs)
        context['userid'] = self.request.user.id
        return context