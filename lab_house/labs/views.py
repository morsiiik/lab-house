from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginUserForm, RegisterUserForm
from .models import *
from .utils import *


# def available_labs(request):
#     context = {
#         'menu': menu,
#         'posts': Lab.objects.filter(is_published=True),
#         'title': 'All labs available'
#     }
#     return render(request, 'labs/index.html', context=context)


class AvailableLabs(DataMixin, ListView):
    model = Lab
    template_name = 'labs/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Доступные лабораторные")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Lab.objects.filter(is_published=True)


class AllLabs(DataMixin, ListView):
    model = Lab
    template_name = 'labs/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Все лабораторные")
        return dict(list(context.items()) + list(c_def.items()))


class MainPage(DataMixin, ListView):
    model = Lab
    template_name = 'labs/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))


def about(request):
    context = get_user_context(request, title="О сайте")
    return render(request, 'labs/about.html', context=context)


# def lab(request, lab_number):
#     context = {
#         'menu': menu,
#         'curr_lab': get_object_or_404(Lab, pk=lab_number)
#     }
#     return render(request, 'labs/curr_lab.html', context=context)

class ShowLab(DataMixin, DetailView):
    model = Lab
    template_name = 'labs/curr_lab.html'
    # pk_url_kwarg = lab_number  # почему-то не работает
    context_object_name = 'curr_lab'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['curr_lab'])
        return dict(list(context.items()) + list(c_def.items()))



class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'labs/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'labs/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def personal_cabinet(request):
    context = get_user_context(request, title="Личный кабинет")
    return render(request, 'labs/pers_cab.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('login')


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена<h1>")
