from .models import *

menu_staff = [
    {'title': 'All labs', 'url_name': 'all'},
    {'title': 'Labs available', 'url_name': 'labs_av'},
    {'title': 'Stuff', 'url_name': 'stuff'},
    {'title': 'Statistic', 'url_name': 'students_statistic'},
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
            else:
                menu[1]['username'] = self.request.user.username
            context['menu'] = menu
        return context


def check_url(url):
    url = str(url)
    components = url.split('/')  # ['https:', '', 'github.com', '....', '....', 'pull', '1']
    return len(components) == 7 and components[2] == 'github.com' and components[5] == 'pull' and components[
        6].isdigit()


def get_user_lose_deadline_count(student, labs):
    count = 0
    for lab in labs:
        if UserLab.objects.filter(user=student, lab=lab, is_approved=False).exists():
            count += 1
    return count
