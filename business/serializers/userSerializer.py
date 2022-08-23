from dataclasses import fields
from datetime import datetime
from distro import like
from rest_framework import serializers

from ..models.models import TblProcess, TblUsers

# from ..models.tblProcessModel import TblProcess
#from models.tblProcessModel import TblProcess


class UserSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField()

    class Meta:
        model = TblUsers
        fields = ['id','id_process','id_entity','id_charge','id_plan','roleid','name','email','user']
        #fields = ('id','id_process')
        exclude =['create_by_user','status','created','modified']
