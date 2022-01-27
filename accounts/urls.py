from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.UserSignupView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/complete/', views.UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('settings/account/', views.UserUpdateView.as_view(), name='my_account'),
    path('settings/password/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('settings/password/done/', views.UserPasswordChangeDoneView.as_view(), name='password_change_done'),
]
