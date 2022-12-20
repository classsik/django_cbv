from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create', PostCreateView.as_view(), name='create'),
    path('edit/<int:pk>', PostEditView.as_view(), name='edit'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete')
]
