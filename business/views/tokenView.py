import jwt
from datetime import datetime

from rest_framework import generics
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from business.serializers.tokenSerializer import TokenSerializer

from ..models.token import Token
from ..models.models import TblProcess
from .baseMensajeView import BaseMessage

# Form Company List
class TokenCompanyListView(generics.ListAPIView):
    permission_classes = ()
    
    def get(self, request, *args, **kwargs):
        message = BaseMessage
        resultToken = Token.objects.filter(status=True).values('companyId')
        if resultToken.count()>0:
            queryset = TblProcess.objects.exclude(id__in=resultToken)
            # for w in queryset:
            #     # print(w.id)
            #     result_company = TblProcess.objects.filter(id = w.id)
            #     w.name = result_company[0].name
        else:
            queryset = TblProcess.objects.all()
        
        context = {}
        context['company'] = queryset
        return render(request,'companyList.html',context)
        

# Add Token Company
class TokenCreateView(generics.CreateAPIView):
    permission_classes = ()
    serializer_class = TokenSerializer
    def create(self, request, *args, **kwargs): 
        message = BaseMessage
        
        #email = str(self.request.data.get("user")).strip()
        processId = str(self.request.data.get("company")).strip()

        # Check Process Id
        try:
            #result_user = TblUsers.objects.get(email= email)
            result_search = TblProcess.objects.get(id= processId)
            if result_search:  
                # Company has Token
                print(result_search)
                search_token = Token.objects.filter(companyId = result_search.id).filter(status=True)
                if search_token.count() >0:
                    return message.CustomMessage('Empresa ya tiene Token Asignado',"Sistema")
                else:
                    payload = {
                        'id': result_search.id,
                        'name': result_search.name,
                    }
                    jwt_token = {'token': jwt.encode(payload,'SECRET',algorithm='HS256')}
                    # Guardar el Token
                    token = Token(
                        #userId = result_search.userid,
                        companyId = result_search.id,
                        token = jwt_token,
                        status = True,
                        created = datetime.now(),
                    )
                    token.save()
                    return message.CustomMessage('Token Generado exitosamente para La Empresa',"Token Generado exitosamente para la Empresa")
        except TblProcess.DoesNotExist:
            return message.ShowMessage('Empresa no Registrada')
        except Exception as e:
            return message.ErrorMessage(str(e))
