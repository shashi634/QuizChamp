# Generated by Django 2.2.5 on 2019-10-26 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=500)),
                ('EmailId', models.EmailField(blank=True, max_length=254, unique=True)),
                ('IsActived', models.BooleanField(default=False)),
                ('ActivatiedOn', models.DateTimeField(default=None)),
                ('OrganizationId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.Organization')),
            ],
        ),
    ]
