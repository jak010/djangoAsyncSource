from django.conf.urls import url

from .views import (
    SampleView
)

urlpatterns = [
    url(r"test$", SampleView.TestView.as_view())
]
