# Generated by Django 3.1.4 on 2021-01-03 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doubts', '0002_auto_20210103_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_dept',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='user_id',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
