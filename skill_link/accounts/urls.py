from django.urls import path
from . import views
from .views import RegisterUser  


urlpatterns = [
    # Example placeholder URL
    path('', views.UserProfileList.as_view(), name='user-profile-list'),
    path('register/', RegisterUser.as_view(), name='register'),

]
