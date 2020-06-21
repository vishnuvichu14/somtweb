from django.urls import path

from .views import ApiLogin,ApiRegistration,ApiUpdateProfile

urlpatterns = [
    path('login/',ApiLogin.as_view(),name="api_login"),
    path('register/',ApiRegistration.as_view(),name="api_registration"),
    path('updated_profile/',ApiUpdateProfile.as_view(),name="api_update_profile"),
]
