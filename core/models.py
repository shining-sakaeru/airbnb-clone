from django.db import models
from . import managers


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(
        auto_now_add=True
    )  # auto_now_add는 model update되면 시간을 자동 저장해줌
    updated = models.DateTimeField(auto_now_add=True)
    objects = managers.CustomModelManager()

    class Meta:
        abstract = True
        # abstract(추상) : model이지만 db에는 나타나지 않는 모델. Code에서만 쓰임
