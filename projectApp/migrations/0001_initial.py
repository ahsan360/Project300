# Generated by Django 3.2.7 on 2021-10-09 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=100)),
                ('uemail', models.EmailField(max_length=100)),
                ('upass', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=500)),
                ('coment', models.CharField(max_length=100)),
            ],
        ),
    ]