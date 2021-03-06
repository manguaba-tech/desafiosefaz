# Generated by Django 3.1.2 on 2020-10-10 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo', models.CharField(max_length=50, verbose_name='Campo')),
                ('valor', models.CharField(max_length=50, verbose_name='Valor')),
            ],
        ),
        migrations.CreateModel(
            name='Classificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado', models.BooleanField(default=False, verbose_name='Resultado')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.produto')),
                ('regra', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='processamento.regra')),
            ],
        ),
    ]
