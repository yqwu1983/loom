# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-17 18:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_fix_notification_context'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileresource',
            name='data_object',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='file_resource', to='api.DataObject'),
        ),
        migrations.AlterField(
            model_name='runconnectornode',
            name='data_node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.DataNode'),
        ),
        migrations.AlterField(
            model_name='runinput',
            name='data_node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.DataNode'),
        ),
        migrations.AlterField(
            model_name='runoutput',
            name='data_node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.DataNode'),
        ),
        migrations.AlterField(
            model_name='taskattemptinput',
            name='data_node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.DataNode'),
        ),
        migrations.AlterField(
            model_name='taskattemptoutput',
            name='data_node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.DataNode'),
        ),
        migrations.AlterField(
            model_name='taskinput',
            name='data_node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.DataNode'),
        ),
        migrations.AlterField(
            model_name='taskoutput',
            name='data_node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.DataNode'),
        ),
        migrations.AlterField(
            model_name='template',
            name='steps',
            field=models.ManyToManyField(related_name='parents', through='api.TemplateMembership', to='api.Template'),
        ),
        migrations.AlterField(
            model_name='templateinput',
            name='data_node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.DataNode'),
        ),
        migrations.AlterField(
            model_name='templatemembership',
            name='child_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_templates', to='api.Template'),
        ),
        migrations.AlterField(
            model_name='templatemembership',
            name='parent_template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_templates', to='api.Template'),
        ),
        migrations.AlterField(
            model_name='userinput',
            name='data_node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.DataNode'),
        ),
    ]
