from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views
from rest_auth.views import PasswordResetConfirmView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('restartPassword/', auth_views.PasswordResetView.as_view(),
         name='resetPassword'),
    path('passwordResetDone/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    re_path(r'^rest-auth/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(),
            name='password_reset_confirm'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('user/profile/', views.UserDetailView.as_view(), name='UserProfile'),
    path('user/profile/update', views.UserUpdateView.as_view(), name='UserUpdate'),
    path('user/profile/updateImage',
         views.ProfileUpdateView.as_view(), name='ProfileUpdate'),
]
