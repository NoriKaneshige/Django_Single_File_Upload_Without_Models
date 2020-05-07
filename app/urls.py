from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    # use normal form in view
    path('', views.SingleUploadView.as_view(), name='single_upload'),
]
