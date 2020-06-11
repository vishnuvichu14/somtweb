from django.urls import path

from .views import ApiLogin

urlpatterns = [
    path('login/',ApiLogin.as_view(),name="api_login"),
]
