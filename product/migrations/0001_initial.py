# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name_plural': 'countries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Diamond_class',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('diamond', models.IntegerField(null=True)),
                ('stone', models.IntegerField(null=True)),
                ('stone_string', models.CharField(max_length=50, blank=True)),
                ('uncut_diamond', models.CharField(max_length=50, blank=True)),
                ('making', models.IntegerField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('in_stock', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gold',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('karat', models.IntegerField()),
                ('price_per_gram', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30, blank=True)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('pic', models.ImageField(blank=True, upload_to='product_pics/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.ForeignKey(to='product.Country')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='type_of',
            field=models.ForeignKey(to='product.Type'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entry',
            name='code',
            field=models.ForeignKey(to='product.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entry',
            name='diamond_type',
            field=models.ForeignKey(to='product.Diamond_class'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entry',
            name='karat',
            field=models.ForeignKey(to='product.Gold'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='product.State'),
            preserve_default=True,
        ),
    ]
