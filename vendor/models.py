from django.db import models
from account.models import UserBase
# Create your models here.
class Vendor(models.Model):
    user = models.OneToOneField(UserBase, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=16)

    def __str__(self) -> str:
        return f'{self.business_name} - {self.user}'
    