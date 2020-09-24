# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-19 09:39
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ipn', '0007_auto_20160219_1135'),
        ('auth', '0007_alter_validators_add_error_messages'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=64)),
                ('trial_period', models.PositiveIntegerField(blank=True, null=True)),
                ('trial_unit', models.CharField(choices=[(b'0', 'No trial'), (b'D', 'Day'), (b'W', 'Week'), (b'M', 'Month'), (b'Y', 'Year')], max_length=1, null=True)),
                ('recurrence_period', models.PositiveIntegerField(blank=True, null=True)),
                ('recurrence_unit', models.CharField(choices=[(None, 'No recurrence'), (b'0', 'No trial'), (b'D', 'Day'), (b'W', 'Week'), (b'M', 'Month'), (b'Y', 'Year')], max_length=1, null=True)),
                ('category', models.CharField(default=b'', max_length=64)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
            options={
                'ordering': ('price', '-recurrence_period'),
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('event', models.CharField(editable=False, max_length=100)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=64, null=True)),
                ('comment', models.TextField(blank=True, default=b'')),
                ('ipn', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='ipn.PayPalIPN')),
                ('subscription', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='subscription.Subscription')),
                ('user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='UserSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expires', models.DateField(default=datetime.date.today, null=True)),
                ('active', models.BooleanField(default=True)),
                ('cancelled', models.BooleanField(default=True)),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscription.Subscription')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='usersubscription',
            unique_together=set([('user', 'subscription')]),
        ),
    ]