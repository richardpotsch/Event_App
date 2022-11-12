from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import FormMixin


class SignUpView(CreateView):
    template_name = "user/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

class LoginView(FormMixin, TemplateView):
    template_name = 'user/login.html'
    form_class = AuthenticationForm

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('events')

        messages.error(request, 'Wrong credentials')
        return redirect('login')

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('events')