# Generated by Django 3.1.4 on 2021-01-07 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Doubts', '0029_auto_20210108_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doubts.student'),
        ),
    ]
