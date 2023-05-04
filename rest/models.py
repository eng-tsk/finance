from django.db import models
from django import forms
import uuid

# Create your models here.

class KindChoices(models.Model):

    class Meta:
        db_table = 'rest_kind'

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.description})"

class CurrencyChoices(models.Model):

    class Meta:
        db_table = 'rest_currency'

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.description})"

class History(models.Model):

    class Meta:
        db_table = 'rest_history'

    date = models.DateField(verbose_name='日付')
    pair = models.ForeignKey(CurrencyChoices, on_delete=models.CASCADE, related_name="cur_pair")
    kind = models.ForeignKey(KindChoices, on_delete=models.CASCADE, related_name="kind_pair")
    order = models.FloatField( verbose_name='注文', blank=False, null=False, default=0, )#[validators.MinValueValidator(0.001), validators.MaxValueValidator(999.999)])
    settlement = models.FloatField( verbose_name='決済', blank=False, null=False, default=0, ) #[validators.MinValueValidator(0.001), validators.MaxValueValidator(999.999)])
    pips = models.FloatField( verbose_name='損益', blank=False, null=False, default=0, )#[validators.MinValueValidator(0.001), validators.MaxValueValidator(999.999)])
    profit = models.IntegerField( verbose_name='評価損益', blank=False, null=False, default=0, )#[validators.MinValueValidator(0.001), validators.MaxValueValidator(999.999)])