from dataclasses import fields
from datetime import datetime
from distro import like
from rest_framework import serializers

from ..models.models import TblProcess, TblUsers

# from ..models.tblProcessModel import TblProcess
#from models.tblProcessModel import TblProcess


class BusinessCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = TblProcess
        field = ('idUser','id')
        exclude =['create_by_user','status','created','modified'
        ,'id_entity','name','mobile','color','web','facebook'
        ,'whatsapp','twitter','instagram','linkedin','google'
        ,'iduser','descripcion_general','direccion','banner','departament'
        ,'is360','pais','nombre_boton','url_boton','nombre_seccion'
        ,'url_iframe','video','moneda','tema','plantilla','id_font'
        ,'tag_departamento','id_language','imagen360','seo','mapa'
        ,'siglas','sub_cat','codigo','default_process','url_label','url_content','municipality','logo_user','tour_virtual']

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
        
    #     # Search Data User
    #     process_id = instance.id
    #     result_user = TblUsers.objects.filter(id_process = process_id)
    #     representation['user'] = result_user[0].user
    #     representation['charge'] = result_user[0].charge
    #     representation['whatsapp'] = result_user[0].whatsapp
    #     representation['profile'] = result_user[0].perfil
    #     representation['background_color'] = result_user[0].colorfondo
    #     representation['background_image'] = result_user[0].imagenfondo
    #     representation['user_photo'] = result_user[0].foto
    #     representation['web_site'] = result_user[0].web
    #     representation['facebook'] = result_user[0].facebook
    #     representation['instagram'] = result_user[0].instagram

    #     return representation