# Generated by Django 5.1.4 on 2024-12-16 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_student_field_remove_student_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='adress',
        ),
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
