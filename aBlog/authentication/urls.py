from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupView, name='signup'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView,name='logout'),
    # path('password-reset/', PasswordResetView.as_view(
    #     template_name='users/password_reset.html'), name='password-reset'),
    # path('password-reset/done/', PasswordResetDoneView.as_view(
    #     template_name='users/password_reset_done.html'), name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
    #     template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    # path('password-reset-complete/', PasswordResetCompleteView.as_view(
    #     template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
