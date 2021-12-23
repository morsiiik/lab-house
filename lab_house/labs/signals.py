from django.contrib.auth import user_logged_in
from django.dispatch import receiver

from .models import Lab, UserLab


@receiver(user_logged_in)
def user_signed_up_(request, user, **kwargs):
    if not user.is_staff:
        if not UserLab.objects.filter(user=user).exists():
            labs = Lab.objects.all()
            for l in labs:
                UserLab.objects.create(lab=l, user=user)
