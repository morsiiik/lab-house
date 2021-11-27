from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Lab(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    task = models.TextField(blank=True, verbose_name='Задание')
    url = models.URLField(verbose_name='URL')
    deadline = models.DateField(verbose_name='Дедлайн')
    is_available = models.BooleanField(default=False, verbose_name='Выдана')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lab', kwargs={'lab_number': self.pk})

    class Meta:
        verbose_name = 'Лабораторная'
        verbose_name_plural = 'Лабораторные'
        ordering = ['pk']


class UserLab(models.Model):
    # Lab.UserLabs.all() выведет все лабораторные пользователей, которые ссылаются на объект Lab
    lab = models.ForeignKey(Lab, verbose_name='Лабораторная', on_delete=models.CASCADE,
                            related_name='UsersLabs')
    # User.MyLabs.all() выведет все лабораторные текущего студента
    user = models.ForeignKey(User, verbose_name='Студент', on_delete=models.CASCADE, related_name='MyLabs')
    url = models.URLField(verbose_name='URL', blank=True)
    is_approved = models.BooleanField(default=False, verbose_name='Зачтена')
    is_sent = models.BooleanField(default=False, verbose_name='Отправлена')
    mentor = models.ForeignKey(User, verbose_name='Ментор', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "Лабораторная: {}, Студента: {}".format(self.lab.title, self.user.username)
