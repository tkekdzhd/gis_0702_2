from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


class Subscription(models.Model):
    # on_delete = models.CASCADE: 계정이 삭제되면 구독정보도 삭제되도록 한다(계정에 종속되도록 함)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='subscription', null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='subscription', null=False)
    # 외부정보 = Meta 정보
    class Meta:
        unique_together = ['user', 'project']