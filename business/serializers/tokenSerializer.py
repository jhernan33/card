from dataclasses import fields
from datetime import datetime
from operator import imod
from distro import like
from rest_framework import serializers

from ..models.token import Token
from ..models.models import TblUsers

class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        field = ['userId','token']
        exclude =['status','created','updated','deleted']

    def to_representation(self, instance):
        userid = instance.userId
        result_user = TblUsers.objects.filter(userId = userid)
        # aerea_id = instance.id_area
        # aera = Area.objects.filter(id = aerea_id).values('nombre')
        return {
                'userId': instance.id,
                'token': instance.token,
                'userName': result_user[0]['name'],
                'user': result_user[0]['user'],
                'processId': instance.id_process,
        }