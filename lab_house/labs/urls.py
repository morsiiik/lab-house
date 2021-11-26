from django.urls import path

from .views import *



urlpatterns = [
    path('lab/<int:pk>/', ShowLab.as_view(), name='lab'),  # http://127.0.0.1:8000/lab/
    path('all/', AllLabs.as_view(), name='all'),
    path('labs-available/', AvailableLabs.as_view(), name='labs_av'),
    path('', MainPage.as_view(), name='home'),
    path('about/', about, name='about'),
    path('login/', LoginUser.as_view(), name='login'),
    path('lk/logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('lk/', personal_cabinet, name='lk')
]
