from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from datetime import date

from .forms import LoginUserForm, RegisterUserForm
from .models import *
from .utils import *


class AvailableLabs(DataMixin, ListView):
    model = Lab
    template_name = 'labs/labs_av.html'
    context_object_name = 'labs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Доступные лабораторные")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Lab.objects.filter(is_available=True)


class AllLabs(DataMixin, ListView):
    model = Lab
    template_name = 'labs/labs_all.html'
    context_object_name = 'labs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Все лабораторные")
        return dict(list(context.items()) + list(c_def.items()))


class MainPage(DataMixin, View):
    def get(self, request):
        if self.request.user.is_staff:
            return redirect('all')
        return redirect('labs_av')


class PersonalCabinet(DataMixin, ListView):
    model = UserLab
    template_name = 'labs/pers_cab.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Личный кабинет")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        if self.request.user.is_staff:
            return UserLab.objects.filter(mentor=self.request.user)
        return UserLab.objects.filter(user=self.request.user)


class Materials(DataMixin, ListView):
    model = Material
    template_name = 'labs/materials.html'
    context_object_name = 'materials'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Полезные материалы")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Material.objects.filter(is_actual=True)


class ApproveUserLab(DataMixin, View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied()
        if request.POST.get('check'):
            lab = UserLab.objects.get(user=User.objects.get(username=kwargs.get('username')),
                                      lab=Lab.objects.get(pk=kwargs.get('lab_number')))
            lab.is_approved = True
            lab.save()
            messages.add_message(request, messages.SUCCESS, 'Лабораторная успешно принята')
        return redirect('user_lab', username=kwargs.get('username'), lab_number=kwargs.get('lab_number'))


class SendUserLab(DataMixin, View):
    def post(self, request, *args, **kwargs):
        if request.user.username != kwargs.get('username'):
            raise PermissionDenied()
        user = request.user
        lab_number = kwargs.get('lab_number')
        lab = UserLab.objects.get(user=user, lab=Lab.objects.get(pk=lab_number))
        url = request.POST.get('url')
        if not check_url(url):
            messages.add_message(request, messages.WARNING,
                                 'Отправляйте ссылку на pull request формата https://github.com/..../..../pull/1')
            return redirect('user_lab', username=request.user, lab_number=lab_number)
        lab.url = request.POST.get('url')
        mentors = User.objects.filter(is_staff=True, is_active=True, is_superuser=False)
        if mentors.exists():
            counter = MentorCounter.objects.get(pk=0)
            num = int(MentorCounter.objects.get(pk=0).counter)
            lab.mentor = mentors[num]
            num += 1
            if num == mentors.count():
                counter.counter = 0
            counter.save()
        else:
            lab.mentor = User.objects.filter(is_superuser=True)[0]
        lab.is_sent = True
        lab.save()
        messages.add_message(request, messages.SUCCESS, 'Лабораторная успешно отправлена')
        return redirect('user_lab', username=request.user, lab_number=lab_number)


class ShowLab(DataMixin, DetailView):
    model = Lab
    template_name = 'labs/curr_lab.html'
    pk_url_kwarg = 'lab_number'
    context_object_name = 'curr_lab'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['curr_lab'])
        return dict(list(context.items()) + list(c_def.items()))


class MyLabs(DataMixin, ListView):
    model = UserLab
    template_name = 'labs/my_labs.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='MyLabs')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        labs = UserLab.objects.filter(user=User.objects.get(username=self.kwargs['username']))
        for lab in labs:
            if lab.lab.deadline < date.today():
                lab.lose_deadline = True
            else:
                lab.lose_deadline = False
        return labs


class StudentStatistic(DataMixin, ListView):
    template_name = 'labs/student_statistic.html'
    context_object_name = 'students'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Students Statistic')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        students = User.objects.filter(is_staff=False, is_active=True)
        for student in students:
            student.approved_count = UserLab.objects.filter(user=student, is_approved=True).count()
            student.not_approved_count = UserLab.objects.all().count() - student.approved_count - Lab.objects.filter(
                is_available=False).count()
            student.lose_deadline_count = get_user_lose_deadline_count(student, Lab.objects.filter(
                deadline__range=["2000-12-31", date.today()]))
        return students


class ShowUserLab(DataMixin, DetailView):
    model = UserLab
    template_name = 'labs/user_lab.html'
    context_object_name = 'lab'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['lab'], user=User.objects.get(username=self.kwargs['username']))
        return dict(list(context.items()) + list(c_def.items()))

    def get_object(self, queryset=None, **kwargs):
        return UserLab.objects.get(lab=Lab.objects.get(pk=self.kwargs['lab_number']),
                                   user=User.objects.get(username=self.kwargs['username']))


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


def logout_user(request):
    logout(request)
    return redirect('login')


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена<h1>")
