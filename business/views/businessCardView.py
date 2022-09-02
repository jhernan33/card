import os
import email

from ast import Not
from atexit import register

from operator import ge
from pyexpat import model
from unicodedata import name
from urllib import request

from django.conf import settings
from django.shortcuts import render
from rest_framework import generics, status

from rest_framework.response import Response
from django.core.serializers import serialize
from business.paginations import SmallResultsSetPagination
from business.serializers.businessCardSerializer import BusinessCardSerializer

from business.serializers.tokenSerializer import TokenSerializer

from ..models.token import Token

from .baseMensajeView import BaseMessage
from ..models.models import TblProcess, TblUsers
from ..serializers.userCardSerializer import UserCardSerializer
from django.contrib.auth.tokens import PasswordResetTokenGenerator

import jwt,json
from rest_framework_jwt.utils import jwt_payload_handler
from django.http import HttpResponseRedirect
from django import template
from rest_framework.exceptions import ValidationError

class UsersCardListView(generics.ListAPIView):
    serializer_class = UserCardSerializer
    permission_classes = ()
    queryset = TblProcess.objects.all()

class UsersCardRetrieveView(generics.RetrieveAPIView):
    permission_classes = ()
    serializer_class = UserCardSerializer
    queryset = TblProcess.objects.all()
    lookup_field = 'id'
      
    def retrieve(self, request, *args, **kwargs):
        message = BaseMessage
        try:
            instance = self.get_object()
        except Exception as e:
            return message.NotFoundMessage("Id de Process no Registrada")  
        else:
            serialize = self.get_serializer(instance)
            return message.ShowMessage(self.serializer_class(instance).data)

class UserCardCreateView(generics.CreateAPIView):
    permission_classes = ()
    def create(self, request, *args, **kwargs): 
        message = BaseMessage
        
        email = str(self.request.data.get("user")).strip()
        # Validar el Usuario si Esta Registrado
        try:
            result_user = TblUsers.objects.get(email= email)
            if result_user:  
                # Validar si el Usuario Tiene Token
                search_token = Token.objects.filter(userId = result_user.userid).filter(status=True)
                if search_token.count() >0:
                    return message.CustomMessage('Usuario ya tiene Token Asignado',"Sistema")
                else:
                    payload = {
                        'id': result_user.userid,
                        'email': result_user.email,
                    }
                    jwt_token = {'token': jwt.encode(payload,'SECRET',algorithm='HS256')}
                    # Guardar el Token
                    token = Token(
                        userId = result_user.userid,
                        token = jwt_token,
                        status = True
                    )
                    token.save()
                    return message.CustomMessage('Token Generado exitosamente para el Usuario',"Token Generado exitosamente para el Usuario")
                    # return render(request, 'link.html', {
                    #     'token': token,
                    # })
                    #return HttpResponseRedirect('link.html')

                #return message.ShowMessage('Token:'+str(jwt_token))
            else:
                return message.ShowMessage('Usuario Invalido')
        except Exception as e:
            return message.ErrorMessage(str(e))

class CardCompanyListView(generics.ListAPIView):
    permission_classes = ()
    
    def get(self, request, *args, **kwargs):
        queryset = Token.objects.filter(status=True)
        for w in queryset:
            # result_user = TblUsers.objects.filter(userid = w.userId)
            result_company = TblProcess.objects.filter(id = w.companyId)
            #w.name = result_user[0].name
            #w.email = result_user[0].email
            w.name = result_company[0].name
            w.frontend = settings.FRONTEND
        context = {}
        context['company'] = queryset
        return render(request,'business/home.html',context)

"""
Class List Business Card
"""
class BusinessCardListView(generics.ListAPIView):
    permission_classes =()
    serializer_class = UserCardSerializer
    pagination_class = SmallResultsSetPagination

    def get_queryset(self):
        queryset = TblUsers.objects.none()
        company_name    = self.request.query_params.get("companyName", None)
        company         = self.request.query_params.get("company", None)
        user            = self.request.query_params.get("user", None)
        userName        = self.request.query_params.get("userName", None)

        """
        Search por Company Id
        """        
        if company:
            result_process = TblProcess.objects.filter(id= company)
            if result_process.count()> 0:
                # Search user from de Process
                queryset = TblUsers.get_queryset().filter(id_process = company)
            #return queryset
        """
        Search for Company Name
        """
        if company_name:
            result_process = TblProcess.objects.filter(name=company_name)
            if result_process.count()>0:
                for proc in result_process:
                    id_process = proc.id
                    queryset = TblUsers.get_queryset().filter(id_process = id_process)
            #return queryset
        
        if user:
            # Search user from de Process
            queryset = TblUsers.get_queryset().filter(userid = user)
            #return queryset
        # Searh UserName
        if userName:
            # Search user
            queryset = TblUsers.get_queryset().filter(name = userName)
            
        return queryset

# Form Business Card For Company
class BusinessCardFormListView(generics.ListAPIView):
    permission_classes =()
    serializer_class = UserCardSerializer
    pagination_class = SmallResultsSetPagination

    def get(self, request, *args, **kwargs):
        queryset = Token.objects.filter(status=True)
        for w in queryset:
            result_company = TblProcess.objects.filter(id = w.companyId)
            w.name = result_company[0].name
            w.frontend = settings.FRONTEND
        context = {}
        context['company'] = queryset
        return render(request,'business/CompanyBusinessCard.html',context)

class BusinessCardFormDetailListView(generics.ListAPIView):
    permission_classes =()
    serializer_class = UserCardSerializer
    pagination_class = SmallResultsSetPagination

    def get(self, request, *args, **kwargs):
        queryset = TblUsers.objects.none()
        company_name    = self.request.query_params.get("companyName", None)
        company         = self.request.query_params.get("company", None)
        user            = self.request.query_params.get("user", None)
        userName        = self.request.query_params.get("userName", None)

        """
        Search por Company Id
        """        
        if company:
            result_process = TblProcess.objects.filter(id= company)
            if result_process.count()> 0:
                # Search user from de Process
                queryset = TblUsers.get_queryset().filter(id_process = company)
            #return queryset
        """
        Search for Company Name
        """
        if company_name:
            result_process = TblProcess.objects.filter(name=company_name)
            if result_process.count()>0:
                for proc in result_process:
                    id_process = proc.id
                    queryset = TblUsers.get_queryset().filter(id_process = id_process)
            #return queryset
        
        if user:
            # Search user from de Process
            queryset = TblUsers.get_queryset().filter(userid = user)
            #return queryset
        # Searh UserName
        if userName:
            # Search user
            queryset = TblUsers.get_queryset().filter(name = userName)
            
        context = {}
        context['cards'] = queryset
        context['frontend'] = settings.FRONTEND
        
        return render(request,'business/ListBusinessCard.html',context)