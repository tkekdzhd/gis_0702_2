from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    # CASCADE 종속(User가 삭제되면 프로필도 삭제됨)
    # related_name >>> user.profile로 접근이 가능해짐
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=30, unique=True, null=True)
    message = models.CharField(max_length=200, null=True)

