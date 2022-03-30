# Generated by Django 4.0.2 on 2022-03-17 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opiskelija',
            fields=[
                ('opiskelijanro', models.IntegerField(primary_key=True, serialize=False)),
                ('etunimi', models.CharField(max_length=50)),
                ('sukunimi', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Opiskelija',
                'verbose_name_plural': 'Opiskelijat',
            },
        ),
        migrations.CreateModel(
            name='Tyokalu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nimi', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Työkalu',
                'verbose_name_plural': 'Työkalut',
            },
        ),
        migrations.CreateModel(
            name='Lainaus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lainausaika', models.DateTimeField()),
                ('opiskelijanro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='varasto.opiskelija')),
                ('tyokalu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='varasto.tyokalu')),
            ],
            options={
                'verbose_name': 'Lainaus',
                'verbose_name_plural': 'Lainaukset',
            },
        ),
    ]