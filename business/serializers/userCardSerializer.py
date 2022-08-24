import os
from dataclasses import fields
from datetime import datetime

from django.conf import settings
from django.conf.urls.static import static
from rest_framework import serializers
from ..models.models import TblProcess, TblUsers

class UserCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = TblUsers
        field = ['id','id_process','id_entity','id_charge','id_plan','roleid','name','email','user']
        exclude =['createdby','password']

    def to_representation(self, instance):
        url = settings.WEBSERVER_IMAGES
        representation = super().to_representation(instance)
        representation['user_name'] = instance.name
        representation['profile'] = instance.perfil
        representation['background_color'] = instance.colorfondo

        representation['background_image'] = '' if self.clearImage(instance.imagenfondo) is None else url+self.clearImage(instance.imagenfondo)
        representation['user_photo'] = '' if self.clearImage(instance.foto) is None else url+self.clearImage(instance.foto)
        representation['web_site'] = instance.web
        representation['foto'] = '' if self.clearImage(instance.foto) is None else url+self.clearImage(instance.foto)
        representation['imagenfondo'] = '' if self.clearImage(instance.imagenfondo) is None else url+self.clearImage(instance.imagenfondo)
        return representation
        
    # metoho clear Image
    def clearImage(*arg):
        image = arg[1]
        imageClear = None
        if image is not None:
            position_image = image.rfind('/')
            # print(position_image)
            imageClear = image[position_image+1:len(image)]
        return imageClear
    