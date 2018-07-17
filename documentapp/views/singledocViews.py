from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from documentapp.models import *
from documentapp.forms import *
from django import urls

from django.contrib.auth.models import User

import ipdb

class GetUniqueDataView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    queryset = SingleDocument.objects.all()
    template_name = 'singledoctemplates/getuniquedetails.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GetUniqueDataView, self).get_context_data(**kwargs)
        context['objects']=SingleDocument.objects.filter(user_id=self.kwargs['pk'])
        context['userid'] = self.request.user.id
        context['docid'] = self.kwargs['pk']
        name=User.objects.get(id=self.kwargs['pk'])
        context['username']=name.username
        return context

class SingledocListsView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    queryset =SingleDocument.objects.all()
    template_name = 'singledoctemplates/singledoclists.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SingledocListsView, self).get_context_data(**kwargs)
        context['val']=SingleDocument.objects.filter(user_id=self.request.user.id)
        context['objects']=User.objects.all()
        context['userid']=self.request.user.id
        return context

class add_SingleSocDetails(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = SingleDocument
    form_class = SingleDocumentForm
    template_name = 'singledoctemplates/singledoclist_add.html'
    success_url = urls.reverse_lazy('documentapp:singledoc.list')
    def post(self, request, *args, **kwargs):
        username=self.request.user.get_username()
        credit_form=SingleDocumentForm(request.POST,request.FILES, initial={'user': request.user})
        if credit_form.is_valid():
            credit_card=credit_form.save(commit=False)
            credit_card.user=self.request.user
            credit_card.save()
            return redirect('documentapp:singledoc.list')
        else:
            return redirect('documentapp:loginpage')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(add_SingleSocDetails, self).get_context_data(**kwargs)
        context['userid']=self.request.user.id
        return context

class edit_SingleDocDetails(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url = '/login/'
    model = SingleDocument
    form_class = SingleDocumentForm
    template_name = 'singledoctemplates/singledoclist_edit.html'
    success_url = urls.reverse_lazy('documentapp:singledoc.list')
    def has_permission(self):
        existing_form = SingleDocument.objects.get(pk=self.kwargs['pk'])
        if self.request.user == existing_form.user:
            return True
        else:
            PermissionError
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(edit_SingleDocDetails, self).get_context_data(**kwargs)
        context['userid']=self.request.user.id
        return context

class delete_SingleDocDetails(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    login_url = '/login/'
    model = Document
    template_name = 'singledoctemplates/singledoclist_delete.html'
    success_url = urls.reverse_lazy('documentapp:singledoc.list')
    def has_permission(self):
        detailer = SingleDocument.objects.get(pk=self.kwargs['pk'])
        if self.request.user == detailer.user:
            return True
        else:
            PermissionError
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(delete_SingleDocDetails, self).get_context_data(**kwargs)
        context['userid']=self.request.user.id
        return context