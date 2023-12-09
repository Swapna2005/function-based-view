from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import LoginForm
from django.shortcuts import render

class LoginForm(FormView):
    template_name = 'my_login.html'
    form_class = LoginForm
    success_url = reverse_lazy('success_page')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        # Add your login logic here if needed
        return super().form_valid(form)

def success_page(request):
    return render(request, 'success_page.html')
