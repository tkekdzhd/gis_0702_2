from django.db import models #models는 패키지명

# Create your models here.
class NewModel(models.Model):
    text = models.CharField(max_length=255, null=False)
