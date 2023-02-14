

from django.urls import path
from django.conf.urls.static import static
from users.views import *

urlpatterns = [
    path('signin/', sign_in, name='signin'),
    path('signup/', sign_up, name='signup'),
    path("logout/", logout_v, name="logout")
]

