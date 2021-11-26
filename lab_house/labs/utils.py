from django.db.models import Count

from .models import *

menu = [
    {'title': 'Main', 'url_name': 'home'},
    {'title': 'All labs', 'url_name': 'all'},
    {'title': 'Labs available', 'url_name': 'labs_av'},
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Login', 'url_name': 'login'},
    {'title': 'Register', 'url_name': 'register'},
    {'title': 'Personal Cabinet', 'url_name': 'lk'}
]


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()

        if self.request.user.is_authenticated:
            # Вроде костыльно а вроде и норм
            user_menu.pop(4)
            user_menu.pop(4)

        else:
            user_menu.pop(6)

        context['menu'] = user_menu
        return context


# не знаю как убрать дублирование кода
def get_user_context(request, **kwargs):
    context = kwargs
    user_menu = menu.copy()

    if request.user.is_authenticated:
        # Вроде костыльно а вроде и норм
        user_menu.pop(4)
        user_menu.pop(4)

    else:
        user_menu.pop(6)

    context['menu'] = user_menu
    return context
