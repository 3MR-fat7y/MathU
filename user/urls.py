from django.urls import path
from .views import (index, user_login, user_logout, user_signup)
# Create your views here.
urlpatterns = [
    path('', index, name='home'),
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/', user_logout, name='logout'),
]

# from django.conf.urls.static import static
# from django.conf import settings
# if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)