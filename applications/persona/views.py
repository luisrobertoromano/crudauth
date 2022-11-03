from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse
from .forms import LoginForm, PersonaForm
from .models import Persona

from django.views.generic import (
    View,
    CreateView,
    TemplateView,
    ListView,
    DetailView
)

from django.views.generic.edit import (
    FormView
)
# Create your views here.

#Vistas para autenticacion
class LoginUser(FormView):
    template_name = 'persona/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('persona_app:user-panel')
    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)

class Panel(LoginRequiredMixin, TemplateView):
    template_name = "persona/panel.html"
    login_url = reverse_lazy('persona_app:user-login')

class LogoutView(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'persona_app:user-login'
            )
        )


class PersonaListView(LoginRequiredMixin,ListView):
    model = Persona
    template_name = "persona/lista.html"
    context_object_name = 'personas'


class PersonaCreateView(LoginRequiredMixin,CreateView):
    model = Persona
    template_name = "persona/add.html"
    form_class = PersonaForm
    success_url = reverse_lazy('persona_app:lista')

