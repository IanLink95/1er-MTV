# Generated by Django 4.0.4 on 2022-05-30 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrodefamiliares', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familiar',
            name='id_nacionalidad',
        ),
        migrations.RemoveField(
            model_name='familiar',
            name='id_parentezco',
        ),
        migrations.DeleteModel(
            name='Nacionalidad',
        ),
        migrations.DeleteModel(
            name='Parentezco',
        ),
    ]