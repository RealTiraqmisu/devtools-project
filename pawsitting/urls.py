from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("login/", LoginView.as_view(template_name='login.html'), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("index/", views.IndexView.as_view(), name="index_page"),
    path("detail/<int:id>/", views.DetailView.as_view(), name="detail_page"),
    path("profile/", views.ProfileView.as_view(), name="profile")
]