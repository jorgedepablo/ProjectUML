# Generated by Django 3.2 on 2022-04-12 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymkhana', '0006_auto_20220328_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diagrams',
            old_name='type',
            new_name='diagram_type',
        ),
    ]