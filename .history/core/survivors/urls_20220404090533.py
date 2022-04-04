from django.urls import path

from .views import *

app_name = 'core.survivors'

urlpatterns = [
    path(
        '',
        SurvivorsView.as_view(),
        name='survivors-actions'
    ),
    path(
        '<int:id>/',
        SurvivorsUpdateView.as_view(),
        name='survivors-details'
    ),
    path(
        'reports/',
        SurvivorsReportView.as_view(),
        name='survivors-report'
    )