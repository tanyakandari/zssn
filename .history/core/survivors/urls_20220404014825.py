from django.urls import path

from core.survivors.views import views

app_name = 'core.survivors'

urlpatterns = [
    path(
        '',
        views.SurvivorsView.as_view(),
        name='survivors-details'
    ),
]