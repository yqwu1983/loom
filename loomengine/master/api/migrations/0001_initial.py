# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-23 19:46
from __future__ import unicode_literals

import api.models
import api.models.base
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArrayMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('order', models.IntegerField()),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='DataNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('uuid', models.CharField(default=api.models.uuidstr, editable=False, max_length=255, unique=True)),
                ('index', models.IntegerField(null=True)),
                ('degree', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='DataObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('uuid', models.CharField(default=api.models.uuidstr, editable=False, max_length=255, unique=True)),
                ('type', models.CharField(choices=[(b'boolean', b'Boolean'), (b'file', b'File'), (b'float', b'Float'), (b'integer', b'Integer'), (b'string', b'String')], max_length=255)),
                ('is_array', models.BooleanField(default=False)),
                ('datetime_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='FileResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('uuid', models.CharField(default=api.models.uuidstr, editable=False, max_length=255, unique=True)),
                ('datetime_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('file_url', models.CharField(max_length=1000)),
                ('md5', models.CharField(max_length=255)),
                ('upload_status', models.CharField(choices=[(b'incomplete', b'Incomplete'), (b'complete', b'Complete'), (b'failed', b'Failed')], default=b'incomplete', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='FixedStepInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('channel', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[(b'boolean', b'Boolean'), (b'file', b'File'), (b'float', b'Float'), (b'integer', b'Integer'), (b'string', b'String')], max_length=255)),
                ('mode', models.CharField(default=b'no_gather', max_length=255)),
                ('group', models.IntegerField(default=0)),
                ('data_root', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.DataNode')),
            ],
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='FixedWorkflowInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('channel', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[(b'boolean', b'Boolean'), (b'file', b'File'), (b'float', b'Float'), (b'integer', b'Integer'), (b'string', b'String')], max_length=255)),
                ('data_root', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.DataNode')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('uuid', models.CharField(default=api.models.uuidstr, editable=False, max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[(b'step', b'Step'), (b'workflow', b'Workflow')], max_length=255)),
                ('datetime_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('datetime_finished', models.DateTimeField(null=True)),
                ('postprocessing_status', models.CharField(choices=[(b'waiting', b'Waiting'), (b'in_progress', b'In progress'), (b'done', b'Done'), (b'error', b'Error')], default=b'saving', max_length=255)),
                ('status_is_finished', models.BooleanField(default=False)),
                ('status_is_failed', models.BooleanField(default=False)),
                ('status_is_killed', models.BooleanField(default=False)),
                ('status_is_running', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='RunRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('datetime_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='RunRequestInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('channel', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[(b'boolean', b'Boolean'), (b'file', b'File'), (b'float', b'Float'), (b'integer', b'Integer'), (b'string', b'String')], max_length=255)),
                ('data_root', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.DataNode')),
                ('run_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inputs', to='api.RunRequest')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='StepRunInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('channel', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[(b'boolean', b'Boolean'), (b'file', b'File'), (b'float', b'Float'), (b'integer', b'Integer'), (b'string', b'String')], max_length=255)),
                ('mode', models.CharField(max_length=255)),
                ('group', models.IntegerField()),
                ('data_root', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.DataNode')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='StepRunOutput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('channel', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[(b'boolean', b'Boolean'), (b'file', b'File'), (b'float', b'Float'), (b'integer', b'Integer'), (b'string', b'String')], max_length=255)),
                ('mode', models.CharField(max_length=255)),
                ('source', jsonfield.fields.JSONField(null=True)),
                ('data_root', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.DataNode')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('uuid', models.CharField(default=api.models.uuidstr, editable=False, max_length=255, unique=True)),
                ('datetime_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('interpreter', models.CharField(default=b'/bin/bash', max_length=255)),
                ('interpreter_options', models.CharField(default=b'-euo pipefail', max_length=1024)),
                ('command', models.TextField()),
                ('rendered_command', models.TextField()),
                ('status_is_running', models.BooleanField(default=True)),
                ('status_is_killed', models.BooleanField(default=False)),
                ('status_is_finished', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='TaskAttempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('uuid', models.CharField(default=api.models.uuidstr, editable=False, max_length=255, unique=True)),
                ('datetime_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('datetime_finished', models.DateTimeField(null=True)),
                ('last_heartbeat', models.DateTimeField(auto_now=True)),
                ('status_is_failed', models.BooleanField(default=False)),
                ('status_is_finished', models.BooleanField(default=False)),
                ('status_is_killed', models.BooleanField(default=False)),
                ('status_is_running', models.BooleanField(default=True)),
                ('status_is_cleaned_up', models.BooleanField(default=False)),
                ('status_message', models.CharField(default=b'Starting', max_length=255)),
                ('status_message_detail', models.CharField(default=b'', max_length=255)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_attempts', to='api.Task')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='TaskAttemptError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('message', models.CharField(max_length=255)),
                ('detail', models.TextField(blank=True, null=True)),
                ('task_attempt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='errors', to='api.TaskAttempt')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='TaskAttemptLogFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('log_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='TaskAttemptOutput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('channel', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[(b'boolean', b'Boolean'), (b'file', b'File'), (b'float', b'Float'), (b'integer', b'Integer'), (b'string', b'String')], max_length=255)),
                ('source', jsonfield.fields.JSONField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='TaskAttemptTimepoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('message', models.CharField(max_length=255)),
                ('task_attempt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timepoints', to='api.TaskAttempt')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='TaskEnvironment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('docker_image', models.CharField(max_length=255)),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='environment', to='api.Task')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='TaskInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('channel', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[(b'boolean', b'Boolean'), (b'file', b'File'), (b'float', b'Float'), (b'integer', b'Integer'), (b'string', b'String')], max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='TaskOutput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('channel', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[(b'boolean', b'Boolean'), (b'file', b'File'), (b'float', b'Float'), (b'integer', b'Integer'), (b'string', b'String')], max_length=255)),
                ('source', jsonfield.fields.JSONField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='TaskResourceSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('memory', models.CharField(max_length=255, null=True)),
                ('disk_size', models.CharField(max_length=255, null=True)),
                ('cores', models.CharField(max_length=255, null=True)),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='api.Task')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('uuid', models.CharField(default=api.models.uuidstr, editable=False, max_length=255, unique=True)),
                ('type', models.CharField(choices=[(b'workflow', b'Workflow'), (b'step', b'Step')], max_length=255)),
                ('datetime_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('name', models.CharField(max_length=255)),
                ('postprocessing_status', models.CharField(choices=[(b'waiting', b'Waiting'), (b'in_progress', b'In progress'), (b'done', b'Done'), (b'error', b'Error')], default=b'saving', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='WorkflowMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='WorkflowRunConnectorNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('channel', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[(b'boolean', b'Boolean'), (b'file', b'File'), (b'float', b'Float'), (b'integer', b'Integer'), (b'string', b'String')], max_length=255)),
                ('data_root', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.DataNode')),
            ],
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='WorkflowRunInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('channel', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[(b'boolean', b'Boolean'), (b'file', b'File'), (b'float', b'Float'), (b'integer', b'Integer'), (b'string', b'String')], max_length=255)),
                ('data_root', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.DataNode')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='WorkflowRunOutput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_change', models.IntegerField(default=0)),
                ('channel', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[(b'boolean', b'Boolean'), (b'file', b'File'), (b'float', b'Float'), (b'integer', b'Integer'), (b'string', b'String')], max_length=255)),
                ('data_root', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.DataNode')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, api.models.base._ModelNameMixin, api.models.base._FilterMixin),
        ),
        migrations.CreateModel(
            name='BooleanDataObject',
            fields=[
                ('dataobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.DataObject')),
                ('value', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
            bases=('api.dataobject',),
        ),
        migrations.CreateModel(
            name='DataObjectArray',
            fields=[
                ('dataobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.DataObject')),
            ],
            options={
                'abstract': False,
            },
            bases=('api.dataobject',),
        ),
        migrations.CreateModel(
            name='FileDataObject',
            fields=[
                ('dataobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.DataObject')),
                ('filename', models.CharField(max_length=1024)),
                ('md5', models.CharField(max_length=255)),
                ('source_type', models.CharField(choices=[(b'imported', b'Imported'), (b'result', b'Result'), (b'log', b'Log')], max_length=255)),
                ('file_import', jsonfield.fields.JSONField(null=True)),
                ('file_resource', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_data_objects', to='api.FileResource')),
            ],
            options={
                'abstract': False,
            },
            bases=('api.dataobject',),
        ),
        migrations.CreateModel(
            name='FloatDataObject',
            fields=[
                ('dataobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.DataObject')),
                ('value', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
            bases=('api.dataobject',),
        ),
        migrations.CreateModel(
            name='IntegerDataObject',
            fields=[
                ('dataobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.DataObject')),
                ('value', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=('api.dataobject',),
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('template_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Template')),
                ('command', models.TextField()),
                ('interpreter', models.CharField(default=b'/bin/bash', max_length=255)),
                ('interpreter_options', models.CharField(default=b'-euo pipefail', max_length=1024)),
                ('environment', jsonfield.fields.JSONField(null=True)),
                ('outputs', jsonfield.fields.JSONField(null=True)),
                ('inputs', jsonfield.fields.JSONField(null=True)),
                ('resources', jsonfield.fields.JSONField(null=True)),
                ('raw_data', jsonfield.fields.JSONField(null=True)),
                ('template_import', jsonfield.fields.JSONField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('api.template',),
        ),
        migrations.CreateModel(
            name='StepRun',
            fields=[
                ('run_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Run')),
                ('command', models.TextField()),
                ('interpreter', models.CharField(max_length=255)),
                ('interpreter_options', models.CharField(max_length=1024)),
            ],
            options={
                'abstract': False,
            },
            bases=('api.run',),
        ),
        migrations.CreateModel(
            name='StringDataObject',
            fields=[
                ('dataobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.DataObject')),
                ('value', models.TextField(max_length=10000)),
            ],
            options={
                'abstract': False,
            },
            bases=('api.dataobject',),
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('template_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Template')),
                ('outputs', jsonfield.fields.JSONField(null=True)),
                ('inputs', jsonfield.fields.JSONField(null=True)),
                ('raw_data', jsonfield.fields.JSONField(null=True)),
                ('template_import', jsonfield.fields.JSONField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('api.template',),
        ),
        migrations.CreateModel(
            name='WorkflowRun',
            fields=[
                ('run_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Run')),
            ],
            options={
                'abstract': False,
            },
            bases=('api.run',),
        ),
        migrations.AddField(
            model_name='workflowmembership',
            name='child_template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='api.Template'),
        ),
        migrations.AddField(
            model_name='taskoutput',
            name='data_object',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.DataObject'),
        ),
        migrations.AddField(
            model_name='taskoutput',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outputs', to='api.Task'),
        ),
        migrations.AddField(
            model_name='taskinput',
            name='data_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.DataObject'),
        ),
        migrations.AddField(
            model_name='taskinput',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inputs', to='api.Task'),
        ),
        migrations.AddField(
            model_name='taskattemptoutput',
            name='data_object',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='task_attempt_output', to='api.DataObject'),
        ),
        migrations.AddField(
            model_name='taskattemptoutput',
            name='task_attempt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outputs', to='api.TaskAttempt'),
        ),
        migrations.AddField(
            model_name='taskattemptlogfile',
            name='file',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='task_attempt_log_file', to='api.DataObject'),
        ),
        migrations.AddField(
            model_name='taskattemptlogfile',
            name='task_attempt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log_files', to='api.TaskAttempt'),
        ),
        migrations.AddField(
            model_name='task',
            name='selected_task_attempt',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_as_selected', to='api.TaskAttempt'),
        ),
        migrations.AddField(
            model_name='runrequest',
            name='run',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='run_request', to='api.Run'),
        ),
        migrations.AddField(
            model_name='runrequest',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Template'),
        ),
        migrations.AddField(
            model_name='run',
            name='template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='runs', to='api.Template'),
        ),
        migrations.AddField(
            model_name='datanode',
            name='data_object',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_nodes', to='api.DataObject'),
        ),
        migrations.AddField(
            model_name='datanode',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='api.DataNode'),
        ),
        migrations.AddField(
            model_name='datanode',
            name='root_node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='descendants', to='api.DataNode'),
        ),
        migrations.AddField(
            model_name='arraymembership',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_array_membership', to='api.DataObject'),
        ),
        migrations.AddField(
            model_name='workflowrunoutput',
            name='workflow_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outputs', to='api.WorkflowRun'),
        ),
        migrations.AddField(
            model_name='workflowruninput',
            name='workflow_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inputs', to='api.WorkflowRun'),
        ),
        migrations.AddField(
            model_name='workflowrunconnectornode',
            name='workflow_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connectors', to='api.WorkflowRun'),
        ),
        migrations.AddField(
            model_name='workflowmembership',
            name='parent_template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='api.Workflow'),
        ),
        migrations.AddField(
            model_name='workflow',
            name='steps',
            field=models.ManyToManyField(related_name='workflows', through='api.WorkflowMembership', to='api.Template'),
        ),
        migrations.AddField(
            model_name='task',
            name='step_run',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='api.StepRun'),
        ),
        migrations.AddField(
            model_name='steprunoutput',
            name='step_run',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outputs', to='api.StepRun'),
        ),
        migrations.AddField(
            model_name='stepruninput',
            name='step_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inputs', to='api.StepRun'),
        ),
        migrations.AddField(
            model_name='run',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='api.WorkflowRun'),
        ),
        migrations.AddField(
            model_name='fixedworkflowinput',
            name='workflow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fixed_inputs', to='api.Workflow'),
        ),
        migrations.AddField(
            model_name='fixedstepinput',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fixed_inputs', to='api.Step'),
        ),
        migrations.AddField(
            model_name='dataobjectarray',
            name='prefetch_members',
            field=models.ManyToManyField(related_name='arrays', through='api.ArrayMembership', to='api.DataObject'),
        ),
        migrations.AddField(
            model_name='arraymembership',
            name='array',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_array_members_membership', to='api.DataObjectArray'),
        ),
        migrations.AlterUniqueTogether(
            name='workflowrunconnectornode',
            unique_together=set([('workflow_run', 'channel')]),
        ),
    ]
