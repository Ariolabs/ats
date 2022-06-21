from django.db import models
import binascii
import os
from django.utils.translation import gettext_lazy as _
from django.db import models
# Create your models here.


class AppToken(models.Model):
    key = models.CharField(max_length=256, primary_key=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    app = models.OneToOneField('app.App', on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    expire_on = models.DateTimeField(blank=True, null=True,)

    class Meta:
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        s = super().save()   
        return s

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
