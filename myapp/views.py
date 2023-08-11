from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, FormView

from .models import Vehicle


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('vehicle')


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('vehicle')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('vehicle')
        return super(RegisterView, self).get(*args, *kwargs)


class VehicleList(ListView):
    model = Vehicle
    context_object_name = 'vehicles'
    template_name = 'list.html'


class AdminVehicleList(ListView):
    model = Vehicle
    context_object_name = 'vehicles'
    template_name = 'adminlistview.html'


class VehicleUpdate(LoginRequiredMixin, UpdateView):
    model = Vehicle
    fields = '__all__'
    success_url = reverse_lazy('vehicle')
    template_name = 'vehiclecreate.html'

def home(request):
    return render(request,'home.html')
