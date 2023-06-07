from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='index'),
    # path('api/v1/post', PostAPIView.as_view(), name='PostAPIView'),
    path('api1/', PostAPIView.as_view(), name='PostAPIView'),
    path('api2/', CategoryAPIView.as_view(), name='CategoryAPIView'),
]
