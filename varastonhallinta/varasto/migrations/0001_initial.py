# Generated by Django 4.0.3 on 2022-04-10 14:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tuote',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('viivakoodi', models.CharField(max_length=30)),
                ('nimike', models.CharField(max_length=50)),
                ('hankintapaikka', models.CharField(max_length=50)),
                ('kustannuspaikka', models.CharField(max_length=10)),
                ('tuotekuva', models.BinaryField()),
            ],
            options={
                'verbose_name': 'Tuote',
                'verbose_name_plural': 'Tuotteet',
            },
        ),
        migrations.CreateModel(
            name='Tuoteryhma',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nimi', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tuoteryhmä',
                'verbose_name_plural': 'Tuoteryhmät',
            },
        ),
        migrations.CreateModel(
            name='Varasto',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('varastotyyppi', models.CharField(max_length=30)),
                ('nimi', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Varasto',
                'verbose_name_plural': 'Varastot',
            },
        ),
        migrations.CreateModel(
            name='Varastotapahtuma',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('arkistotunnus', models.CharField(max_length=50, verbose_name='Arkistotunnus')),
                ('maara', models.IntegerField(verbose_name='Määrä')),
                ('aikaleima', models.DateField(default=django.utils.timezone.now, editable=False, verbose_name='Aikaleima')),
                ('palautuspaiva', models.DateField(default=datetime.datetime(2022, 4, 24, 17, 44, 14, 16878), verbose_name='Palautuspäivä')),
                ('asiakas', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='asiakas', to=settings.AUTH_USER_MODEL, verbose_name='Asiakas')),
                ('tuote', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='varasto.tuote', verbose_name='Tuote')),
                ('varasto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='varasto.varasto', verbose_name='Varasto')),
                ('varastonhoitaja', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='varastonhoitaja', to=settings.AUTH_USER_MODEL, verbose_name='Varastonhoitaja')),
            ],
            options={
                'verbose_name': 'Varastotapahtuma',
                'verbose_name_plural': 'Varastotapahtumat',
            },
        ),
        migrations.AddField(
            model_name='tuote',
            name='tuoteryhma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='varasto.tuoteryhma'),
        ),
    ]