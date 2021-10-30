from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from articles.views import *

urlpatterns = [
	path('', main_page),
	path('admin/', admin.site.urls),
	path('articles/', include('articles.urls'))
]

# if in DEBUG then this will enable local media
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# handles 404 error while DEBUG = False
handler404 = page_not_found
