from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PrintItem
from django.shortcuts import render, redirect
from django.contrib import messages
from printers.models import Printer
from django.contrib.auth.decorators import login_required
from .forms import PrintItemCreations

class HomePageView(ListView):
    model = PrintItem
    template_name = 'printing/home.html'
    context_object_name = 'posts'
    ordering = ['-time']
    paginate_by = 2
    

class AboutPageView(TemplateView):
    template_name = 'printing/about.html'
    title = 'About'

class ServicePageView(TemplateView):
    template_name = 'printing/services.html'
    title = 'Services'

class ContactsPageView(TemplateView):
    template_name = 'printing/contact.html'
    title = 'Contacts'


# class PrintCreateView(LoginRequiredMixin, CreateView):
#     model = PrintItem
#     template_name = 'printing/print.html'
#     fields = '__all__'
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

class ViewPrinters(ListView):
    model = Printer
    template_name = 'printing/printers.html'
    context_object_name = 'posts'
    paginate_by = 2


class PrintCreateView(LoginRequiredMixin, CreateView):
    template_name = 'printing/print.html'
    def get(self,request):
        form = PrintItemCreations()
        return render(request, self.template_name, {'form':form})

    def post(self,request):
        form = PrintItemCreations(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')



class PrintCreateView2(LoginRequiredMixin, CreateView):
    template_name = 'printing/print.html'
    model = PrintItem
    fields = ['upload','pages','copies','printer', 'owner']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    