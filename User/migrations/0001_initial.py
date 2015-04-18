# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('placed_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('type_s', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('profile_pic', models.ImageField(upload_to='profile_pics/', blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=10)),
                ('address', models.CharField(max_length=50)),
                ('cart_info', models.ManyToManyField(to='product.Entry')),
                ('city', models.ForeignKey(to='product.City')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_status',
            field=models.ForeignKey(to='User.Status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(to='product.Entry'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(to='User.UserProfile'),
            preserve_default=True,
        ),
    ]
