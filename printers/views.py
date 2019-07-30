from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Printer
from printing.models import PrintItem
from .forms import PrinterRegisterForm
from django.contrib import messages

class PrinterHomePageView(ListView):
    model = PrintItem
    template_name = 'printers/home.html'
    context_object_name = 'posts'
    ordering = ['-time']
    paginate_by = 2


class HomePageView(ListView):
    template_name = 'printers/home.html'
    context_object_name = 'posts'
    ordering = ['-time']
    paginate_by = 2
    

class AboutPageView(TemplateView):
    template_name = 'printers/about.html'
    title = 'About'

class ServicePageView(TemplateView):
    template_name = 'printers/services.html'
    title = 'Services'

class ContactsPageView(TemplateView):
    template_name = 'printers/contact.html'
    title = 'Contacts'


class PrinterCreateView(LoginRequiredMixin, CreateView):
    model = Printer
    template_name = 'printers/add_printer.html'
    fields = '__all__'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def register(self, request):
        if request.method == 'POST':
            form = PrinterRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                # username = form.cleaned_data.get('username')
                messages.success(request, f'Your account has been created! You are now able to log in')
                return redirect('home')
        else:
            form = PrinterRegisterForm()
        return render(request, 'users/register.html', {'form': form})

