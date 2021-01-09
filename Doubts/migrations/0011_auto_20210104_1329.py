# Generated by Django 3.1.4 on 2021-01-04 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doubts', '0010_auto_20210104_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answered',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='assigned_teacher',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer_text',
            field=models.CharField(default='Your Question has not been answered yet', max_length=500),
        ),
    ]
