# Generated by Django 3.2.8 on 2021-10-26 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_remove_project_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='sku',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]