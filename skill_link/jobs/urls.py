from django.urls import path
from . import views
from .views import JobPostingListCreate

urlpatterns = [
    
    path('', JobPostingListCreate.as_view(), name='job-list-create'),

]
