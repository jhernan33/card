from django.db import models

class Token(models.Model):
    userId = models.IntegerField(null=True, blank=True)
    token = models.CharField(max_length=255,null=True, blank=True)
    status = models.BooleanField(default=True,null=True, blank=True)
    companyId = models.IntegerField(null=True, blank=True)
    created  =models.DateTimeField(auto_now=False, null=True,auto_now_add=False,blank=True)
    updated  =models.DateTimeField(auto_now=False, null=True,auto_now_add=False,blank=True)
    deleted  =models.DateTimeField(auto_now=False, null=True,auto_now_add=False,blank=True)

    class Meta:
        db_table = 'tbl_token'