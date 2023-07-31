from django.db import models
from django.core.validators import MinLengthValidator


class Company(models.Model):
    name = models.CharField(max_length=256)
    bin = models.CharField(max_length=12, validators=[MinLengthValidator(12)])
    country = models.CharField(max_length=128)
    employee_count = models.PositiveIntegerField(default=0)
    industry = models.ForeignKey('Industry', on_delete=models.CASCADE)
    parent = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class Industry(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Industry'
        verbose_name_plural = 'Industries'
