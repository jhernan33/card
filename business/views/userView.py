from rest_framework import generics, status
from django.shortcuts import render
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from ..serializers.userSerializer import UserSerializer

from ..models.models import TblUsers

class UsersListView(generics.ListAPIView):
    permission_classes = ()
    serializer_class = UserSerializer
    queryset = TblUsers.objects.all()

