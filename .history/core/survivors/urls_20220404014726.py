from django.urls import path

from core.contracts.views import web_views as views

app_name = 'core.survivors'

urlpatterns = [
    path(
        '',
        views.SurvivorsView.as_view(),
        name='survivors-details'
    ),
]