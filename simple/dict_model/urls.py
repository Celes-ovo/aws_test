# from django.conf.urls import url
from django.urls import re_path as url
from .views import TestView


# urlpatterns = [
#     path('test/', TestView().as_view()),
# ]

urlpatterns = [
    url(r'^test/$', TestView.as_view()),
]