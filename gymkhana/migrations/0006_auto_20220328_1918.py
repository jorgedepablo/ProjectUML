# Generated by Django 3.2 on 2022-03-28 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gymkhana', '0005_auto_20211117_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenges',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='challenges/'),
        ),
        migrations.AddField(
            model_name='users',
            name='updated_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='challenges_passed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gymkhana.challenges'),
        ),
    ]