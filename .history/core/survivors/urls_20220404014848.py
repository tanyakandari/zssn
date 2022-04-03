from django.urls import path

from .views import *

app_name = 'core.survivors'

urlpatterns = [
    path(
        '',
        SurvivorsView.as_view(),
        name='survivors-details'
    ),
]