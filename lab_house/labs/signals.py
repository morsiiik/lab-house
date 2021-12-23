from django.contrib.auth import user_logged_in
from django.dispatch import receiver

from .models import Lab, UserLab

'''
Я потратил часа 3, чтобы разобраться почему не работает user_sign_up, для него нужна какая-то отдельная библиотека не 
предустановленная в джанго.
Моя цель была в том, чтобы при регистрации пользователя для него автоматически создавались UserLabs, и он мог приступать 
к решениям.
Я пытался подключить кучу библиотек, но все время ничего не работало, официальная документация тоже несильно помогла
Решил заменить регистрацию на проверку создавались ли раньше лабы при логине. Костыльно немного, но по другому хз как.
'''


@receiver(user_logged_in)
def user_signed_up_(request, user, **kwargs):
    if not user.is_staff:
        if not UserLab.objects.filter(user=user).exists():
            labs = Lab.objects.all()
            for l in labs:
                UserLab.objects.create(lab=l, user=user)
