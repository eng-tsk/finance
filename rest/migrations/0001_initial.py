# Generated by Django 4.2 on 2023-05-04 13:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyChoices',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'rest_currency',
            },
        ),
        migrations.CreateModel(
            name='KindChoices',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'rest_kind',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日付')),
                ('order', models.FloatField(default=0, verbose_name='注文')),
                ('settlement', models.FloatField(default=0, verbose_name='決済')),
                ('pips', models.FloatField(default=0, verbose_name='損益')),
                ('profit', models.IntegerField(default=0, verbose_name='評価損益')),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kind_pair', to='rest.kindchoices')),
                ('pair', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cur_pair', to='rest.currencychoices')),
            ],
            options={
                'db_table': 'rest_history',
            },
        ),
    ]