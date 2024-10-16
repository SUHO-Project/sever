# Generated by Django 4.2.16 on 2024-10-18 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='menuName',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='menuPrice',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='id',
        ),
        migrations.AddField(
            model_name='cart',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.menu'),
        ),
        migrations.AddField(
            model_name='menu',
            name='menuId',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='menuPrice',
            field=models.IntegerField(default=0),
        ),
    ]
