from django.contrib.auth import views as auth_views
from django.urls import path, include
from register import views as v

urlpatterns = [
    path('register/', v.register, name='register'),
    path('register/infos/', v.profile, name='profile'),
    path('login/', v.login_view, name='login'),
    path('logout/', v.logout_view, name='logout'),
    path('register/reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset/password_reset.html"), name="reset_password"),
    path('register/reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset/password_reset_sent.html"), name="password_reset_done"),
    path('register/reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name='password_reset_confirm'),
    path('register/reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset/password_reset_complete.html"), name="password_reset_complete"),
]
