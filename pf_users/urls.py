from django.urls import path, include

from pf_users.views.user import UserViewSet
from rest_framework.routers import DefaultRouter
from pf_users.views.auth import LoginView
from pf_users.views.password_reset import PasswordResetView
from pf_users.views.password_reset_request import PasswordResetRequestView

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name=LoginView.name),
    path('password-reset-request/', PasswordResetRequestView.as_view(), name=PasswordResetRequestView.name),
    path('reset-password/<uidb64>/<token>/', PasswordResetView.as_view(), name=PasswordResetView.name),
]
