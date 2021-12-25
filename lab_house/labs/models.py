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

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            users = User.objects.all()
            for u in users:
                if u.is_active and not u.is_staff:
                    UserLab.objects.create(lab=self, user=u)
        else:
            super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Лабораторная'
        verbose_name_plural = 'Лабораторные'
        ordering = ['pk']


class UserLab(models.Model):
    lab = models.ForeignKey(Lab, verbose_name='Лабораторная', on_delete=models.CASCADE,
                            related_name='UsersLabs')
    user = models.ForeignKey(User, verbose_name='Студент', on_delete=models.CASCADE, related_name='MyLabs')
    url = models.URLField(verbose_name='URL', blank=True)
    is_approved = models.BooleanField(default=False, verbose_name='Зачтена')
    is_sent = models.BooleanField(default=False, verbose_name='Отправлена')
    mentor = models.ForeignKey(User, verbose_name='Ментор', blank=True, null=True, on_delete=models.SET_NULL)
    commits = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('user_lab', kwargs={'username': self.user.username, 'lab_number': self.lab.pk})

    def __str__(self):
        return "Лабораторная: {}, Студента: {}".format(self.lab.title, self.user.username)


class Material(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    url = models.URLField(verbose_name='URL')
    is_actual = models.BooleanField(default=True, verbose_name='Актуальна')

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
        ordering = ['pk']


class Announcement(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Содержимое')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    is_important = models.BooleanField(default=True, verbose_name='Важное')
    is_actual = models.BooleanField(default=True, verbose_name='Актуально')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['pk']


class MentorCounter(models.Model):
    counter = models.PositiveIntegerField(default=0)
