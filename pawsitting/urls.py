from django.urls import path
from . import views
from .views import LoginView, LogoutView


urlpatterns = [
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("index/", views.IndexView.as_view(), name="index_page"),
    path("detail/<int:id>/", views.DetailView.as_view(), name="detail_page"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("sittercentre/", views.SitterCentreView.as_view(), name="sittercentre"),
    path("userbooking/", views.UserBookingView.as_view(), name="userbooking"),
]