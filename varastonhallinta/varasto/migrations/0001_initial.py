# Generated by Django 4.0.3 on 2022-04-05 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Henkilo',
            fields=[
                ('id', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('roolinimitys', models.CharField(choices=[('opettaja', 'Opettaja'), ('oppilas', 'Oppilas')], default='oppilas', max_length=20)),
                ('etunimi', models.CharField(max_length=35)),
                ('sukunimi', models.CharField(max_length=35)),
            ],
            options={
                'verbose_name': 'Henkilö',
                'verbose_name_plural': 'Henkilöt',
            },
        ),
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
                ('arkistotunnus', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('maara', models.IntegerField()),
                ('aikaleima', models.DateField()),
                ('palautuspaiva', models.DateField()),
                ('asiakas', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='asiakas', to='varasto.henkilo')),
                ('tuote', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='varasto.tuote')),
                ('varasto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='varasto.varasto')),
                ('varastonhoitaja', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='varastonhoitaja', to='varasto.henkilo')),
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
