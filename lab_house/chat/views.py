from django.shortcuts import render
from labs.views import *
from .models import Message
from labs.utils import *


def room(request, room_name):
    if not request.user.is_staff:
        raise PermissionDenied()
    username = request.user.username
    messages = Message.objects.filter(room=room_name)[0:50]

    context = {'room_name': room_name, 'username': username, 'mess': messages, 'menu': menu_staff.copy()}
    return render(request, 'chat/room.html', context=context)
