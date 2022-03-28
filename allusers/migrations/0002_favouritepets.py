# Generated by Django 3.2.7 on 2022-03-28 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allpets', '0001_initial'),
        ('allusers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouritePets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allpets.petbreed')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allusers.userprofile')),
            ],
        ),
    ]