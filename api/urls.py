from django.urls import path
from .views import MemberAPIView

urlpatterns = [
    path('', MemberAPIView.as_view())
]