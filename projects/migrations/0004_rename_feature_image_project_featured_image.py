# Generated by Django 4.0.4 on 2022-04-25 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_feature_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='feature_image',
            new_name='featured_image',
        ),
    ]
