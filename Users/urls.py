from django.urls import path, reverse_lazy
from Users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("accounts/register/", views.register, name='register'),
    path("accounts/profile/", auth_views.PasswordChangeView.as_view(template_name="registration/profile.html", success_url = reverse_lazy('home')), name="profile")]
