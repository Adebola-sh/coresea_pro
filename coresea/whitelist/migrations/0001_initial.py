# Generated by Django 4.0.2 on 2023-03-08 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='wl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter', models.CharField(max_length=100)),
                ('metamask', models.CharField(max_length=50)),
                ('nft_address', models.CharField(help_text='Hold any of these NFT \n (Moondogs, CorepunksV2,Core Id)\n Submit wallet address of holding', max_length=50)),
            ],
        ),
    ]
