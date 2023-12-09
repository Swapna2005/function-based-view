from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import RegisterForm
from django.shortcuts import render

class RegisterForm(FormView):
    template_name = 'my_register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('success_page')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email= form.cleaned_data['email']
        password = form.cleaned_data['password']
        # Add your login logic here if needed
        return super().form_valid(form)

def success_page(request):
    return render(request, 'success_page.html')

