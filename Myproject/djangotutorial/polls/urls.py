from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:module_id>/", views.detail, name="detail"),
    path("<int:module_id>/results/", views.results, name="results"),
    path("<int:module_id>/vote/", views.vote, name="vote"),
]
