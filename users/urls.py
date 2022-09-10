from urllib.parse import urlparse
from django.urls import path
from knox import views as knox_views
from . import views

from .views import ShortenerCreateApiView, ShortenerListAPIView

from users.url_views.register_views import register_api
from users.url_views.login_views import login_api
from users.url_views.user_views import get_user_data


app_name = "users"   


urlpatterns = [
    
    path('login/', login_api),
    path('user/', get_user_data),
    path('register/', register_api),
    path('logout/', knox_views.LogoutView.as_view()),

    path('',ShortenerListAPIView.as_view(),name='all_links'),

    # Original URL to Short URL
    path('create_short_url/',ShortenerCreateApiView.as_view(),name='create_api'),

]
