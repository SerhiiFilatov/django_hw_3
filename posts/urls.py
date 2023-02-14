

from django.urls import path
from django.conf.urls.static import static
from posts.views import homepage, list_detail_view

urlpatterns = [
    path('', homepage, name='home'),
    path('<slug:p_slug>/', list_detail_view, name='det_v')
]

