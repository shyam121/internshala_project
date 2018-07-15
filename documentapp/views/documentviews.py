from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from documentapp.models import *
from documentapp.forms import *
from django import urls

def regview(request):
    return render(request=request,template_name = 'documenttemplates/details_list.html')

def Mainpage(request):
    return render(request=request, template_name='mainpage.html')


class details_list(LoginRequiredMixin,ListView):
    login_url = '/login/'
    # model = Document
    queryset =Document.objects.all()
    template_name = 'documenttemplates/details_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(details_list, self).get_context_data(**kwargs)
        context['val']=Document.objects.filter(pk=self.request.user.id)
        context['userid']=self.request.user.id
        return context

class add_details(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = Document
    form_class = DocumentForm
    template_name = 'documenttemplates/details_add.html'
    success_url = urls.reverse_lazy('documentapp:details.list')
    def post(self, request, *args, **kwargs):
        username=self.request.user.get_username()
        credit_form=DocumentForm(request.POST,request.FILES, initial={'user': request.user})
        if credit_form.is_valid():
            credit_card=credit_form.save(commit=False)
            credit_card.user=self.request.user
            credit_card.save()
            return redirect('documentapp:details.list')
        else:
            return redirect('documentapp:loginpage')

class edit_details(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url = '/login/'
    model = Document
    form_class = DocumentForm
    template_name = 'documenttemplates/details_edit.html'
    success_url = urls.reverse_lazy('documentapp:details.list')
    def has_permission(self):
        existing_form = Document.objects.get(pk=self.kwargs['pk'])
        if self.request.user == existing_form.user:
            return True
        else:
            PermissionError

class delete_Details(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    login_url = '/login/'
    model = Document
    template_name = 'documenttemplates/details_delete.html'
    success_url = urls.reverse_lazy('documentapp:details.list')
    def has_permission(self):
        detailer = Document.objects.get(pk=self.kwargs['pk'])
        if self.request.user == detailer.user:
            return True
        else:
            PermissionError