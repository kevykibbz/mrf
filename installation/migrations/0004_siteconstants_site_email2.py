# Generated by Django 3.2.9 on 2022-06-08 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installation', '0003_auto_20220608_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconstants',
            name='site_email2',
            field=models.CharField(blank=True, default='example@gmail.com', max_length=100, null=True),
        ),
    ]