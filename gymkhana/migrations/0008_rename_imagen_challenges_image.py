# Generated by Django 3.2 on 2022-04-12 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymkhana', '0007_rename_type_diagrams_diagram_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challenges',
            old_name='imagen',
            new_name='image',
        ),
    ]