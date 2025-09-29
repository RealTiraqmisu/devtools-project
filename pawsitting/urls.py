from django.urls import path
from . import views
urlpatterns = [
    path("index/", views.IndexView.as_view(), name="index_page"),
    path("detail/<int:id>/", views.DetailView.as_view(), name="detail_page")
]