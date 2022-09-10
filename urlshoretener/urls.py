
from django.contrib import admin
from django.urls import path, include
from users import views


from users.views import Redirector

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),

    
    path('<str:shortener_link>/', Redirector.as_view(), name='redirector')
]
