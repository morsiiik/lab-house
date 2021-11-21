from django.db import models
from django.urls import reverse


class Lab(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    task = models.TextField(blank=True, verbose_name='Задание')
    url = models.URLField(verbose_name='URL')
    deadline = models.DateField(verbose_name='Дедлайн')
    is_published = models.BooleanField(default=False, verbose_name='Выдана')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lab', kwargs={'lab_number': self.pk})

    class Meta:
        verbose_name = 'Лабораторная'
        verbose_name_plural = 'Лабораторные'
        ordering = ['pk']
