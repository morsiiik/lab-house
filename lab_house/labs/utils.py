from django.db.models import Count

from .models import *

menu_staff = [
    {'title': 'All labs', 'url_name': 'all'},
    {'title': 'Labs available', 'url_name': 'labs_av'},
    {'title': 'Stuff', 'url_name': 'stuff'},
]

menu_user = [
    {'title': 'All labs', 'url_name': 'labs_av'},
    {'title': 'My labs', 'url_name': 'my_labs'},
    {'title': 'Stuff', 'url_name': 'stuff'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        if self.request.user.is_staff:
            context['menu'] = menu_staff.copy()
        else:
            menu = menu_user.copy()
            if not self.request.user.is_authenticated:
                menu.pop(1)
            context['menu'] = menu
        return context
