from django.db import models

class Token(models.Model):
    userId = models.IntegerField(null=False, blank=False)
    token = models.CharField(max_length=255,null=True, blank=True)
    status = models.BooleanField(default=True,null=True, blank=True)

    class Meta:
        db_table = 'tbl_token'