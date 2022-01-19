from django.contrib import admin
from django.urls import path, include
from .views import HomepageView, SignupView
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetDoneView, PasswordResetConfirmView,
    PasswordResetCompleteView, PasswordResetView
)

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('', include('leads.urls', namespace='leads')),
    path('', include('agents.urls', namespace='agents')),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset-password', PasswordResetView.as_view(), name='reset-password'),
    path('password-reset-done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('admin/', admin.site.urls),
]
