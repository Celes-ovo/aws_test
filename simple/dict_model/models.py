from django.db import models

# Create your models here.
# our modules

# random한 dictionary를 반환하는 모델
class MyModel(models.Model):
    def get_dict(self):
        return {"Landmark": "(123, 456), (789, 012)"}
    class Meta:
        verbose_name = "MyModel"
        verbose_name_plural = "MyModels"