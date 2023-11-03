from django.contrib.auth.models import AbstractUser
from django.db import models

class Enterprise(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Organization(models.Model):
    name = models.CharField(max_length=30)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.DO_NOTHING, null=True, blank=True )

    def __str__(self):
        return f"{self.name}"

class WorkCenter(models.Model):
    name = models.CharField(max_length=20)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.organization}"
class User(AbstractUser):
    is_administrator = models.BooleanField(default=False)
    organization = models.ForeignKey("Organization", on_delete=models.DO_NOTHING, null=True, blank=True)
    work_center = models.ForeignKey("WorkCenter", on_delete=models.DO_NOTHING, null=True, blank=True)

