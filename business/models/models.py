# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
# * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser

class TblAchievement(models.Model):
    id = models.AutoField(primary_key=True)
    id_process = models.IntegerField(blank=True, null=True)
    id_entity = models.IntegerField()
    name = models.CharField(max_length=150)
    description = models.TextField()
    status = models.IntegerField()
    imagen = models.CharField(max_length=255, blank=True, null=True)
    video = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    real_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    expiration = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()
    imagen2 = models.CharField(max_length=255)
    imagen3 = models.CharField(max_length=255)
    imagen4 = models.CharField(max_length=255)
    id_language = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_achievement'


class TblAxis(models.Model):
    id = models.AutoField(primary_key=True)
    id_entity = models.IntegerField()
    id_process = models.IntegerField(blank=True, null=True)
    id_categorie = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    status = models.IntegerField()
    imagen = models.CharField(max_length=255, blank=True, null=True)
    video = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    real_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    created = models.DateTimeField()
    imagen2 = models.CharField(max_length=255)
    imagen3 = models.CharField(max_length=255)
    imagen4 = models.CharField(max_length=255)
    id_language = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_axis'


class TblBloggin(models.Model):
    title = models.CharField(max_length=80, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_to_publish = models.DateField(blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    id_user = models.IntegerField(blank=True, null=True)
    id_bloggin_categorie = models.IntegerField(blank=True, null=True)
    imagen = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_bloggin'


class TblBlogginCategories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    slug = models.CharField(max_length=80, blank=True, null=True)
    id_super = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_bloggin_categories'


class TblCategories(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_categories'


class TblCategoriesProcess(models.Model):
    # id = models.AutoField(unique=True)
    cat = models.CharField(max_length=100, blank=True, null=True)
    sub_cat = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_categories_process'


class TblCharges(models.Model):
    # id = models.AutoField(unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    id_entity = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_charges'


class TblClients(models.Model):
    # id = models.AutoField(unique=True)
    id_entity = models.IntegerField(blank=True, null=True)
    id_process = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    id_language = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_clients'


class TblConfiguration(models.Model):
    id = models.AutoField(primary_key=True)
    from_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    port = models.CharField(max_length=100, blank=True, null=True)
    host = models.CharField(max_length=100, blank=True, null=True)
    mail_body_massive = models.TextField(blank=True, null=True)
    email2 = models.CharField(max_length=255)
    password2 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tbl_configuration'


class TblDepartamentMunicipality(models.Model):
    id = models.AutoField(primary_key=True)
    departament = models.CharField(max_length=100, blank=True, null=True)
    municipality = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_departament_municipality'


class TblEncuesta(models.Model):
    # id = models.AutoField(unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    id_user = models.IntegerField(blank=True, null=True)
    id_process = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    id_language = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_encuesta'


class TblEncuestaOpciones(models.Model):
    # id = models.AutoField(unique=True)
    id_encuesta = models.CharField(max_length=255, blank=True, null=True)
    opciones = models.CharField(max_length=255, blank=True, null=True)
    emoji = models.CharField(max_length=255, blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_encuesta_opciones'


class TblEntity(models.Model):
    id = models.AutoField(primary_key=True)
    id_plan = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.DateField()
    status = models.IntegerField()
    name_achievement = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField()
    name_axis = models.CharField(max_length=50, blank=True, null=True)
    name_client = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tbl_entity'


class TblEntityUsers(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.IntegerField(blank=True, null=True)
    id_entity = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_entity_users'


class TblFormContact(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    message = models.CharField(max_length=2000, blank=True, null=True)
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    id_process = models.IntegerField(blank=True, null=True)
    id_entity = models.CharField(max_length=45, blank=True, null=True)
    date_row = models.DateTimeField(blank=True, null=True)
    type_form = models.IntegerField(blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    whatsapp = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_form_contact'


class TblGlobalConfiguration(models.Model):
    img_login = models.CharField(max_length=255, blank=True, null=True)
    img_logo = models.CharField(max_length=255, blank=True, null=True)
    title_login = models.CharField(max_length=255, blank=True, null=True)
    img_favicon = models.CharField(max_length=255, blank=True, null=True)
    name_app = models.CharField(max_length=100, blank=True, null=True)
    about_us = models.TextField(blank=True, null=True)
    terms_and_conditions = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    web = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    google = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    img_profile_default = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_global_configuration'


class TblGoogleFonts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tbl_google_fonts'


class TblLanguage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    folder = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    created = models.DateTimeField()
    active = models.IntegerField()
    siglas = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tbl_language'


class TblLocal(models.Model):
    id = models.AutoField(primary_key=True)
    id_storey = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    id_tower = models.IntegerField(blank=True, null=True)
    id_type_local = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    id_process = models.IntegerField(blank=True, null=True)
    id_user = models.IntegerField(blank=True, null=True)
    coefficient = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_local'


class TblNameItems(models.Model):
    # id = models.AutoField(unique=True)
    producto = models.CharField(max_length=255)
    servicio = models.CharField(max_length=255)
    cliente = models.CharField(max_length=255)
    id_user = models.IntegerField()
    descripcion_producto = models.TextField()
    descripcion_servicio = models.TextField()
    descripcion_cliente = models.TextField()
    id_language = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_name_items'


class TblPlans(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    num_process = models.IntegerField(blank=True, null=True)
    num_users = models.IntegerField(blank=True, null=True)
    num_axis = models.IntegerField(blank=True, null=True)
    num_achievement = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    visible = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_plans'


class TblPlansAsignacion(models.Model):
    # id = models.AutoField(unique=True)
    nombre = models.CharField(max_length=255)
    id_user = models.IntegerField()
    num_achievement = models.IntegerField()
    num_axis = models.IntegerField()
    num_process = models.IntegerField()
    num_users = models.IntegerField()
    created = models.DateTimeField()
    id_plan = models.ForeignKey(TblPlans, models.DO_NOTHING, db_column='id_plan')

    class Meta:
        managed = False
        db_table = 'tbl_plans_asignacion'


class TblProcess(models.Model):
    id = models.AutoField(primary_key=True)
    iduser = models.IntegerField(db_column='idUser')  # Field name made lowercase.
    id_entity = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=150)
    descripcion_general = models.TextField(blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    banner = models.CharField(max_length=255, blank=True, null=True)
    imagen360 = models.CharField(max_length=255, blank=True, null=True)
    is360 = models.IntegerField()
    color = models.CharField(max_length=255, blank=True, null=True)
    seo = models.CharField(max_length=255, blank=True, null=True)
    mapa = models.TextField(blank=True, null=True)
    siglas = models.CharField(max_length=50, blank=True, null=True)
    sub_cat = models.CharField(max_length=100, blank=True, null=True)
    codigo = models.CharField(max_length=40, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    web = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    whatsapp = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    google = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    departament = models.CharField(max_length=200, blank=True, null=True)
    municipality = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    default_process = models.IntegerField(blank=True, null=True)
    url_label = models.CharField(max_length=100, blank=True, null=True)
    url_content = models.CharField(max_length=255, blank=True, null=True)
    logo_user = models.CharField(max_length=255, blank=True, null=True)
    tour_virtual = models.TextField(blank=True, null=True)
    create_by_user = models.IntegerField(blank=True, null=True)
    pais = models.CharField(max_length=255)
    nombre_boton = models.CharField(max_length=255)
    url_boton = models.CharField(max_length=255)
    nombre_seccion = models.CharField(max_length=255)
    url_iframe = models.CharField(max_length=255)
    video = models.TextField()
    moneda = models.CharField(max_length=255)
    tema = models.IntegerField()
    plantilla = models.IntegerField()
    id_font = models.IntegerField()
    tag_departamento = models.CharField(max_length=255)
    id_language = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_process'
    
    def get_queryset():
        return TblProcess.objects.all().filter(status__isnull=True)


class TblProcessDetail(models.Model):
    id_process = models.IntegerField(blank=True, null=True)
    slogan_app = models.CharField(max_length=150, blank=True, null=True)
    logo_app = models.CharField(max_length=255, blank=True, null=True)
    email_process = models.CharField(max_length=150, blank=True, null=True)
    longitud = models.CharField(max_length=255, blank=True, null=True)
    latitud = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_process_detail'


class TblResetPassword(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=128)
    activation_id = models.CharField(max_length=32)
    agent = models.CharField(max_length=512)
    client_ip = models.CharField(max_length=32)
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.
    createdby = models.BigIntegerField(db_column='createdBy')  # Field name made lowercase.
    createddtm = models.DateTimeField(db_column='createdDtm')  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy', blank=True, null=True)  # Field name made lowercase.
    updateddtm = models.DateTimeField(db_column='updatedDtm', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_reset_password'


class TblRoles(models.Model):
    # roleid = models.AutoField(db_column='roleId', primary_key=True)  # Field name made lowercase.
    role = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tbl_roles'


class TblSchedule(models.Model):
    id = models.AutoField(primary_key=True)
    id_process = models.IntegerField(blank=True, null=True)
    day = models.CharField(max_length=50, blank=True, null=True)
    first_time = models.TimeField(blank=True, null=True)
    last_time = models.TimeField(blank=True, null=True)
    free = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_schedule'


class TblStorey(models.Model):
    id = models.AutoField(primary_key=True)
    id_tower = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_storey'


class TblSuscribe(models.Model):
    # id = models.AutoField(unique=True)
    correo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_suscribe'


class TblTarjetasDigitales(models.Model):
    # id = models.AutoField(unique=True)
    id_user_logged = models.IntegerField()
    id_user_tarjeta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_tarjetas_digitales'


class TblTarjetasFisicas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    empresa = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    url_image = models.CharField(max_length=255)
    web = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    id_user = models.IntegerField()
    id_app = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_tarjetas_fisicas'


class TblTipoDeFuentes(models.Model):
    fuente = models.CharField(max_length=255, blank=True, null=True)
    dir_fuente = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_tipo_de_fuentes'


class TblTower(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_tower'


class TblTypeLocal(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_type_local'


class TblUsers(models.Model):
    userid = models.AutoField(primary_key=True)  # Field name made lowercase.
    id_process = models.IntegerField(blank=True, null=True)
    id_entity = models.IntegerField(blank=True, null=True)
    id_charge = models.IntegerField(blank=True, null=True)
    id_plan = models.IntegerField(blank=True, null=True)
    roleid = models.IntegerField(db_column='roleId')  # Field name made lowercase.
    name = models.CharField(max_length=128, blank=True, null=True)
    email = models.CharField(max_length=128,unique=True )
    user = models.CharField(max_length=150, blank=True, null=True)
    password = models.CharField(max_length=128)
    foto = models.CharField(max_length=255, blank=True, null=True)
    qr = models.CharField(max_length=255, blank=True, null=True)
    perfil = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    whatsapp = models.CharField(max_length=100, blank=True, null=True)
    phone_code = models.CharField(max_length=50, blank=True, null=True)
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.
    createdby = models.IntegerField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    createddtm = models.DateTimeField(db_column='createdDtm', blank=True, null=True)  # Field name made lowercase.
    updateddtm = models.DateTimeField(db_column='updatedDtm', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.IntegerField(db_column='updatedBy', blank=True, null=True)  # Field name made lowercase.
    web = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    google = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    local_phone = models.CharField(max_length=50, blank=True, null=True)
    charge = models.CharField(max_length=150, blank=True, null=True)
    original_password = models.CharField(max_length=150, blank=True, null=True)
    token_password = models.CharField(max_length=255, blank=True, null=True)
    pre_mobile = models.CharField(max_length=5, blank=True, null=True)
    pre_whatsapp = models.CharField(max_length=5, blank=True, null=True)
    date_tarjeta = models.DateTimeField(blank=True, null=True)
    tema = models.IntegerField()
    plantilla = models.IntegerField()
    user_access = models.IntegerField()
    id_language = models.IntegerField()
    id_language_selected = models.IntegerField()
    multiuser = models.IntegerField()
    original_user = models.IntegerField()
    colorfondo = models.CharField(db_column='colorFondo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    imagenfondo = models.CharField(db_column='ImagenFondo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        managed = False
        db_table = 'tbl_users'
        ordering = ['-userid']
    
    def get_queryset():
        return TblUsers.objects.all().filter(isdeleted__isnull=False)


class TblUsers3D(models.Model):
    userid = models.IntegerField(unique=True)  # Field name made lowercase.
    id_process = models.IntegerField()
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    whatsapp = models.CharField(max_length=255)
    id_charge = models.IntegerField()
    perfil = models.TextField()
    foto = models.CharField(max_length=255)
    web = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    google = models.CharField(max_length=255)
    createdby = models.IntegerField(db_column='createdBy')  # Field name made lowercase.
    created = models.DateTimeField()
    id_language = models.IntegerField()
    multiuser = models.IntegerField()
    original_user = models.IntegerField()
    charge = models.CharField(max_length=255)
    date_tarjeta = models.DateTimeField()
    id_tarjeta = models.IntegerField()
    user = models.CharField(max_length=255)
    user_link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_users_3d'


class TblUsuarioTarjeta(models.Model):
    id_user = models.IntegerField()
    id_axis_achievement = models.IntegerField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_usuario_tarjeta'


class TblVisits(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.IntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    browser = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    date_row = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_visits'


class TblVisits3D(models.Model):
    # id = models.AutoField(unique=True)
    browser = models.CharField(max_length=255)
    id_user = models.IntegerField()
    ip_address = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    date_row = models.DateField()

    class Meta:
        managed = False
        db_table = 'tbl_visits_3d'


class TblVotacion(models.Model):
    # id = models.AutoField(unique=True)
    id_encuesta = models.CharField(max_length=255, blank=True, null=True)
    id_voto_op = models.IntegerField(blank=True, null=True)
    id_user = models.IntegerField(blank=True, null=True)
    id_user_tpd = models.IntegerField(blank=True, null=True)
    voto_coe = models.FloatField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    observation = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_votacion'
