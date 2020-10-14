# Generated by Django 3.1.2 on 2020-10-13 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20201013_2232'),
        ('processamento', '0002_auto_20201012_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classificacao',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.produto'),
        ),
        migrations.AlterField(
            model_name='classificacao',
            name='regra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processamento.regra'),
        ),
    ]