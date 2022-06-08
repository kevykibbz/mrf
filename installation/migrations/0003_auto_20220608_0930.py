# Generated by Django 3.2.9 on 2022-06-08 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installation', '0002_auto_20220531_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteconstants',
            name='special_hours',
        ),
        migrations.AddField(
            model_name='siteconstants',
            name='binge',
            field=models.URLField(blank=True, default='https://www.binge.com', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='siteconstants',
            name='facebook',
            field=models.URLField(blank=True, default='https://web.facebook.com/kevy.kibbz/', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='siteconstants',
            name='instagram',
            field=models.URLField(blank=True, default='https://www.instagram.com/kevviey/', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='siteconstants',
            name='linkedin',
            field=models.URLField(blank=True, default='https://www.linkedin.com/in/chill-cash-260aba206/', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='siteconstants',
            name='twitter',
            field=models.URLField(blank=True, default='https://twitter.com/Kevin36285655', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='siteconstants',
            name='whatsapp',
            field=models.URLField(blank=True, default='https://wa.link/r9fxm4', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='siteconstants',
            name='youtube',
            field=models.URLField(blank=True, default='https://youtube.com', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='siteconstants',
            name='description',
            field=models.TextField(blank=True, default='Madras Rubber Factory(MRF) is a Tyre manufacturer that produces a wide range of tyres. Its specializes in Car & bike tyres trucks/buses tires, LCV & SCV(light & small commercial vehicle) tires, farm services & OTR tyres.', null=True),
        ),
        migrations.AlterField(
            model_name='siteconstants',
            name='site_email',
            field=models.CharField(blank=True, default='mudrasrubberfactory@gmail.com', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='siteconstants',
            name='site_name',
            field=models.CharField(blank=True, default='MudrasRubberFactory', max_length=100, null=True),
        ),
    ]