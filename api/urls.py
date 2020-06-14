from django.urls import path

from .views import ApiLogin,ApiRegistration

urlpatterns = [
    path('login/',ApiLogin.as_view(),name="api_login"),
    path('register/',ApiRegistration.as_view(),name="api_registration"),
]
