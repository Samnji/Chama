from rest_framework import generics
from .serializers import MemberSerializer

from members.models import Member

class MemberAPIView(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
