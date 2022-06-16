from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from users.views import login, register


urlpatterns = [
    path('login', login, name="login"),
    path('register', register, name="register")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
